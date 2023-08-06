import copy
import logging
from collections import OrderedDict
from collections import namedtuple
from platform import platform, system
from sys import version_info as vi

import backoff
from requests import Session
from requests.exceptions import ConnectionError, RequestException, Timeout, TooManyRedirects

from sequoia import __version__ as client_version, util
from sequoia import env, error
from sequoia.auth import BYOTokenAuth

RETRY_HTTP_STATUS_CODES = 'retry_http_status_codes'

MAX_TOKEN_RETRIES = 3

try:
    from distro import linux_distribution
except ImportError:
    def linux_distribution():
        return '', '', '', ''

try:
    from platform import win32_ver
except ImportError:
    def win32_ver():
        return '', '', '', ''

try:
    from platform import mac_ver
except ImportError:
    def mac_ver():
        return '', '', '', ''


class HttpExecutor:
    os_info = platform()
    os_versions = {
        'Linux': "%s (%s)" % (linux_distribution()[0], os_info),
        'Windows': "%s (%s)" % (win32_ver()[0], os_info),
        'Darwin': "%s (%s)" % (mac_ver()[0], os_info),
    }

    user_agent = 'sequoia-client-sdk-python/%s python/%s %s/%s' % (
        client_version,
        '%s.%s.%s' % (vi.major, vi.minor, vi.micro),
        system(),
        os_versions.get(system(), ''),
    )

    MAX_TIME_SECONDS = 120
    DEFAULT_BACKOFF_CONF = {'interval': 0, 'max_tries': 10}

    # pylint: disable-msg=too-many-arguments
    def __init__(self, auth, session=None, proxies=None, user_agent=None, get_delay=None, request_timeout=None,
                 backoff_strategy=None, correlation_id=None, user_id=None, application_id=None, content_type=None):
        self.logger = logging.getLogger(__name__)
        if user_agent is not None:
            self.user_agent = user_agent + self.user_agent

        self._set_backoff_strategy(backoff_strategy, HttpExecutor.DEFAULT_BACKOFF_CONF)

        self.get_delay = get_delay
        self.session = session or Session()
        self.session.proxies = proxies or {}
        self.session.auth = auth

        self.user_id = user_id
        self.application_id = application_id
        self.correlation_id = correlation_id

        self.common_headers = {
            'User-Agent': self.user_agent,
            "Content-Type": content_type or 'application/vnd.piksel+json',
            "Accept": content_type or 'application/vnd.piksel+json',
            "X-Correlation-ID": self.correlation_id
        }

        self.request_timeout = request_timeout or env.DEFAULT_REQUEST_TIMEOUT_SECONDS

    def _set_backoff_strategy(self, backoff_strategy, default_backoff_strategy):
        self.backoff_strategy = copy.deepcopy(backoff_strategy) or default_backoff_strategy
        self.backoff_max_time = self.backoff_strategy.pop('max_time', self.MAX_TIME_SECONDS) or self.MAX_TIME_SECONDS

    @staticmethod
    def create_http_error(response):
        try:
            ret = response.json()
        except ValueError as e:
            ret = "An unexpected error occurred. HTTP Status code: %s. " % response.status_code
            ret += "Error message: %s. " % e
        return error.HttpError(ret, response.status_code)

    @staticmethod
    def return_response(response, resource_name):
        return HttpResponse(response, resource_name)

    # TODO retry_when_empty_result deprecated, it should be a key of the backoff_strategy dictionary. When removed
    #  get rid of the pylint disable-too-many-locals
    # pylint: disable=too-many-locals
    def request(self, method, url, data=None, params=None, headers=None, retry_count=0, resource_name=None,
                retry_when_empty_result=None, backoff_strategy=None):

        if retry_when_empty_result:
            self.logger.warning('The use of `retry_when_empty_result` parameter directly is deprecated '
                                'and will be removed in future releases, '
                                'please use it as a key of the dictionary `backoff_strategy`.')

        _backoff_strategy = copy.deepcopy(self.backoff_strategy) if not backoff_strategy else backoff_strategy
        _backoff_max_time = _backoff_strategy.pop('max_time', self.backoff_max_time)
        _retry_when_empty_result = _backoff_strategy.pop('retry_when_empty_result') \
            if 'retry_when_empty_result' in _backoff_strategy else retry_when_empty_result

        if 'retry_when_empty_result' in _backoff_strategy and retry_when_empty_result:
            self.logger.warning('The `retry_when_empty_result` within `backoff_strategy` precedes the direct '
                                'argument `retry_when_empty_result`, which will be deprecated in a future release.')

        def http_status_codes_to_retry():
            retry_codes = _backoff_strategy.pop(RETRY_HTTP_STATUS_CODES, [])
            retry_codes = list(map(int, retry_codes)) if isinstance(retry_codes, (list, tuple)) else [int(retry_codes)]
            retry_codes.append(429)
            return retry_codes

        retry_http_status_codes = http_status_codes_to_retry()

        def fatal_code(e):
            return isinstance(e, error.AuthorisationError) or \
                   isinstance(e, error.HttpError) and \
                   400 <= e.status_code < 500 and \
                   e.status_code not in retry_http_status_codes

        def _response_does_not_have_data(ret):
            linked_resources_have_data = [False]
            if 'linked' in ret.data and _retry_when_empty_result and isinstance(_retry_when_empty_result, dict):
                linked_resources_have_data = [(k in ret.data['linked'] and not bool(ret.data['linked'][k]))
                                              for k, v in _retry_when_empty_result.items() if v]
            elif 'linked' in ret.data and _retry_when_empty_result:
                linked_resources_have_data = [not bool(ret.data['linked'][k])
                                              for k in ret.data['linked'].keys()]

            main_resource_has_data = ret.resource_name and not bool(ret.data[ret.resource_name])
            return main_resource_has_data or any(linked_resources_have_data)

        def backoff_handler(details):
            self.logger.warning('Retry `%s` (%.1fs) for args `%s` and kwargs `%s`', details['tries'], details['wait'],
                                details['args'], details['kwargs'])

        def backoff_giveup_handler(details):
            self.logger.error('Backoff giving up after %d tries', details['tries'])

        decorated_request = backoff.on_exception(
            _backoff_strategy.pop('wait_gen', backoff.constant),
            (error.ConnectionError, error.Timeout, error.TooManyRedirects, error.HttpError),
            max_time=_backoff_max_time,
            giveup=fatal_code,
            on_backoff=backoff_handler,
            on_giveup=backoff_giveup_handler,
            **copy.deepcopy(_backoff_strategy)
        )(self._request)

        if _retry_when_empty_result:
            decorated_request = backoff.on_predicate(
                wait_gen=_backoff_strategy.pop('wait_gen', backoff.constant),
                predicate=_response_does_not_have_data,
                max_time=_backoff_max_time,
                on_backoff=backoff_handler,
                on_giveup=backoff_giveup_handler,
                **copy.deepcopy(_backoff_strategy)
            )(decorated_request)

        return decorated_request(method, url, data=data,
                                 params=params, headers=headers,
                                 retry_count=retry_count,
                                 resource_name=resource_name)

    def _request(self, method, url, data=None, params=None, headers=None, retry_count=0,
                 token_retry_count=0, resource_name=None):
        request_headers = util.merge_dicts(self.common_headers, headers)
        if params:
            params = OrderedDict(sorted(params.items()))

        try:
            response = self.session.request(
                method, url, data=data, params=params, headers=request_headers, allow_redirects=False,
                timeout=self.request_timeout)
        except RequestException as request_exception:
            raise self._raise_sequoia_error(request_error=request_exception)
        except error.TokenExpiredError as e:
            self.logger.info('Token Expired Error: `%s`', str(e))
            self.logger.info('Updating token and retrying request')
            return self._update_token_and_retry_request(method, url, data=data, params=params,
                                                        headers=request_headers, retry_count=retry_count,
                                                        resource_name=resource_name)

        if response.is_redirect:
            return self.request(method, response.headers['location'], data=data, params=params, headers=request_headers,
                                retry_count=retry_count, resource_name=resource_name)

        if response.status_code == 401 \
            and not isinstance(self.session.auth, BYOTokenAuth) \
            and token_retry_count < MAX_TOKEN_RETRIES:
            self.logger.info('Updating token and retrying request')
            return self._update_token_and_retry_request(method, url, data=data, params=params,
                                                        headers=request_headers, retry_count=retry_count,
                                                        token_retry_count=token_retry_count + 1,
                                                        resource_name=resource_name)

        if 400 <= response.status_code <= 600:
            self._raise_sequoia_error(response)

        return self.return_response(response, resource_name=resource_name)

    def _update_token_and_retry_request(self, *request_args, **request_kwargs):
        try:
            # This can raise AuthorisationError and should not be retried
            self.session.auth.update_token()
            return self._request(*request_args, **request_kwargs)
        except NotImplementedError:
            raise error.TokenExpiredError("Session does not provide update_token capability")

    def _raise_sequoia_error(self, response=None, request_error=None):
        if isinstance(request_error, ConnectionError):
            raise error.ConnectionError(str(request_error.args[0]), cause=request_error)
        if isinstance(request_error, Timeout):
            raise error.Timeout(str(request_error.args[0]), cause=request_error)
        if isinstance(request_error, TooManyRedirects):
            raise error.TooManyRedirects(str(request_error.args[0]), cause=request_error)
        # error with status code
        raise self.create_http_error(response)

    def get(self, url, params=None, resource_name=None, retry_when_empty_result=None, backoff_strategy=None):
        return self.request('GET', url, params=params, resource_name=resource_name,
                            retry_when_empty_result=retry_when_empty_result, backoff_strategy=backoff_strategy)

    def post(self, url, data, params=None, headers=None, resource_name=None):
        return self.request('POST', url, data=util.wrap(data, resource_name), params=params, headers=headers,
                            resource_name=resource_name)

    def put(self, url, data, params=None, headers=None, resource_name=None):
        return self.request('PUT', url, data=util.wrap(data, resource_name), params=params, headers=headers,
                            resource_name=resource_name)

    def delete(self, url, params=None, resource_name=None):
        return self.request('DELETE', url, params=params, resource_name=resource_name)


class HttpResponse(object):
    """Wraps the response object providing raw access via the
    underscore prefix, e.g. _status_code. The response data object
    is available via the _data_ property.
    """

    def __init__(self, response, resource_name=None, model_builder=None):
        self.logger = logging.getLogger(__name__)
        self.resource_name = resource_name
        self.raw = response
        if response.text:
            self.json = response.json()
            self.full_json = self.json
            if model_builder and resource_name:
                self.model = model_builder(self.json, resource_name)
            if resource_name:
                # fixme Remove unwrapping
                self.json = util.unwrap(self.json, resource_name)
            self.logger.debug("Got JSON response with status code `%s`", response.status_code)

    @property
    def data(self):
        return self.full_json

    @property
    def resources(self):
        if self.resource_name:
            return self.json
        return None

    @property
    def status(self):
        return self.raw.status_code

    def to_object(self):
        json_object = self.raw.json(object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        return getattr(json_object, self.resource_name)

    def __getattr__(self, item):
        if item.startswith("_"):
            return getattr(self.raw, item[1:])
        return self.__dict__.get(item, None)
