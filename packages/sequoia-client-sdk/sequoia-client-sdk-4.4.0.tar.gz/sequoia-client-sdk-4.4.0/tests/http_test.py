import unittest
from unittest import mock
from unittest.mock import Mock, call, patch

import pytest
import requests
import requests_mock
from hamcrest import assert_that, equal_to, instance_of, is_, is_in, none, starts_with

from sequoia import auth, error, http


class HttpExecutorTest(unittest.TestCase):
    def setUp(self):
        self.session_mock = requests.Session()
        self.adapter = requests_mock.Adapter()
        self.session_mock.mount('mock', self.adapter)

    @patch('requests.Session')
    def test_request_given_a_list_of_parameters_then_they_are_added_to_the_request(self, session_mock):
        # There is an issue where parameters won't be added to the request if the prefix does not start
        # with http https://bugs.launchpad.net/requests-mock/+bug/1518497. So request-mock can't be used here
        # to check parameters
        session_mock.request.return_value.url = 'mock://some_url'
        session_mock.request.return_value.status_code = 200
        session_mock.request.return_value.is_redirect = False
        my_user_agent = 'my_user_agent'

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=session_mock, correlation_id="my_correlation_id",
                                          user_agent=my_user_agent,
                                          content_type="application/json")

        http_executor.request("POST", "mock://some_url",
                              data='some data',
                              headers={'New-Header': 'SomeValue'},
                              params={'key1': 'value1'})

        expected_headers = {
            'User-Agent': http_executor.user_agent,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Correlation-ID": "my_correlation_id",
            "New-Header": 'SomeValue'
        }

        session_mock.request.assert_called_with('POST', 'mock://some_url', allow_redirects=False, data='some data',
                                                headers=expected_headers, params={'key1': 'value1'}, timeout=240)
        assert_that(http_executor.user_agent, starts_with(my_user_agent))

    @staticmethod
    def match_request_text(request):
        return 'some data' in (request.text or '')

    def test_request_given_additional_headers_and_data_then_they_are_added_to_the_request(self):
        self.adapter.register_uri('POST', 'mock://some_url', text='{"key_1": "value_1"}',
                                  request_headers={'New-Header': 'SomeValue'},
                                  additional_matcher=HttpExecutorTest.match_request_text)

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)
        response = http_executor.request("POST", "mock://some_url",
                                         headers={'New-Header': 'SomeValue'},
                                         data='some data')

        assert_that(response.data, equal_to({"key_1": "value_1"}))

    def test_request_given_get_method_and_an_unreachable_url_then_a_connectivity_error_should_be_raised(self):
        self.adapter.register_uri('GET', 'mock://some_url',
                                  exc=requests.exceptions.ConnectionError('some error desc'))

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)

        with pytest.raises(error.ConnectionError) as sequoia_error:
            http_executor.request("GET", "mock://some_url")

        assert_that('some error desc', is_in(sequoia_error.value.args))
        assert_that(sequoia_error.value.cause, instance_of(requests.exceptions.ConnectionError))

    def test_request_given_server_returns_too_many_redirects_then_error_should_be_raised(self):
        self.adapter.register_uri('GET', 'mock://some_url',
                                  exc=requests.exceptions.TooManyRedirects('some error desc'))

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)

        with pytest.raises(error.TooManyRedirects) as sequoia_error:
            http_executor.request("GET", "mock://some_url")

        assert_that('some error desc', is_in(sequoia_error.value.args))
        assert_that(sequoia_error.value.cause, instance_of(requests.exceptions.TooManyRedirects))

    def test_request_given_get_method_and_server_throw_connection_timeout_then_a_connection_error_should_be_raised(
        self):
        self.adapter.register_uri('GET', 'mock://some_url',
                                  exc=requests.exceptions.ConnectTimeout('some error desc'))

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)

        with pytest.raises(error.ConnectionError) as sequoia_error:
            http_executor.request("GET", "mock://some_url")

        assert_that('some error desc', is_in(sequoia_error.value.args))
        assert_that(sequoia_error.value.cause, instance_of(requests.exceptions.ConnectionError))

    def test_request_given_get_method_and_server_throw_timeout_then_a_timeout_error_should_be_raised(self):
        self.adapter.register_uri('GET', 'mock://some_url',
                                  exc=requests.exceptions.Timeout('some error desc'))

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)

        with pytest.raises(error.Timeout) as sequoia_error:
            http_executor.request("GET", "mock://some_url")

        assert_that('some error desc', is_in(sequoia_error.value.args))
        assert_that(sequoia_error.value.cause, instance_of(requests.exceptions.Timeout))

    def test_request_given_get_method_and_server_returns_an_error_code_then_that_error_should_be_populated(self):
        self.adapter.register_uri('GET', 'mock://test.com', text='some json value', status_code=403)

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)

        with pytest.raises(error.HttpError) as sequoia_error:
            http_executor.request("GET", "mock://test.com")

        assert_that(sequoia_error.value.status_code, 403)
        assert_that(sequoia_error.value.message, 'some json value')
        assert_that(sequoia_error.value.cause, none())

    def test_request_given_post_method_and_server_returns_an_error_code_then_that_error_should_be_populated(self):
        self.adapter.register_uri('POST', 'mock://test.com', text='{"error": "some json value"}', status_code=403)

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)

        with pytest.raises(error.HttpError) as sequoia_error:
            http_executor.request("POST", "mock://test.com")

        assert_that(sequoia_error.value.status_code, is_(403))
        assert_that(sequoia_error.value.message, is_({'error': 'some json value'}))
        assert_that(sequoia_error.value.cause, none())

    def test_request_given_server_returns_an_error_then_the_request_should_be_retried(self):
        json_response = {"resp2": "resp2"}
        self.adapter.register_uri('GET', 'mock://test.com',
                                  [
                                      {'text': 'resp1', 'status_code': 500},
                                      {'json': json_response, 'status_code': 200}
                                  ])

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)
        response = http_executor.request("GET", "mock://test.com")

        assert_that(response.data, equal_to(json_response))

    def test_request_given_server_returns_an_error_then_the_request_should_be_retried_10_times_by_default(self):
        json_response = '{"resp2": "resp2"}'

        self.adapter.register_uri('GET', 'mock://test.com', [{'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': json_response, 'status_code': 200}])

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)
        with pytest.raises(error.HttpError) as sequoia_error:
            http_executor.request("GET", "mock://test.com")

        assert_that(sequoia_error.value.status_code, is_(500))

    def test_request_given_server_returns_an_error_then_the_request_should_be_retried_configured_times_by_default(self):
        json_response = {"resp2": "resp2"}

        self.adapter.register_uri('GET', 'mock://test.com', [{'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'text': 'resp1', 'status_code': 500},
                                                             {'json': json_response, 'status_code': 200}])

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock,
                                          backoff_strategy={'interval': 0, 'max_tries': 11})
        response = http_executor.request("GET", "mock://test.com")

        assert_that(response.data, equal_to(json_response))

    def test_request_given_server_returns_an_error_due_to_token_expired_then_the_request_should_be_retried(self):
        json_response = {"resp2": "resp2"}

        mock_response_500 = Mock()
        mock_response_500.is_redirect = False
        mock_response_500.status_code = 500
        mock_response_500.return_value.json = json_response

        mock_response_200 = Mock()
        mock_response_200.is_redirect = False
        mock_response_200.status_code = 200
        mock_response_200.json.return_value = json_response

        mock_auth = Mock()
        mock_session = Mock()
        mock_session.request.side_effect = [error.TokenExpiredError('Token Expired'),
                                            mock_response_500,
                                            mock_response_200]

        http_executor = http.HttpExecutor(mock_auth,
                                          session=mock_session,
                                          backoff_strategy={'interval': 0, 'max_tries': 2})
        response = http_executor.request("GET", "mock://test.com")

        assert_that(response.data, equal_to(json_response))

        call_list = [call('GET', 'mock://test.com', allow_redirects=False, data=None,
                          headers={'User-Agent': mock.ANY, 'Content-Type': 'application/vnd.piksel+json',
                                   'Accept': 'application/vnd.piksel+json', 'X-Correlation-ID': None}, params=None,
                          timeout=240),
                     call('GET', 'mock://test.com', allow_redirects=False, data=None,
                          headers={'User-Agent': mock.ANY, 'Content-Type': 'application/vnd.piksel+json',
                                   'Accept': 'application/vnd.piksel+json', 'X-Correlation-ID': None}, params=None,
                          timeout=240),
                     call('GET', 'mock://test.com', allow_redirects=False, data=None,
                          headers={'User-Agent': mock.ANY, 'Content-Type': 'application/vnd.piksel+json',
                                   'Accept': 'application/vnd.piksel+json', 'X-Correlation-ID': None}, params=None,
                          timeout=240)]

        assert_that(mock_session.request.call_count, is_(3))
        mock_session.request.assert_has_calls(call_list)

        assert_that(mock_session.auth.update_token.call_count, is_(1))

    def test_request_given_server_returns_an_token_expired_error_then_the_request_should_be_retried(self):
        """
        Testing the use of an invalid token and how the client-sdk should automatically get a new token.
        There are two type of errors when a new token is automatically retrieved: getting the TokenExpiredError exception
        and getting a valid response from the service with a 401 and using the auth method of providing credentials.

        This unit test checks both types: the exception and the 401 status error.
        """
        json_response = {"resp2": "resp2"}

        mock_response_401 = Mock()
        mock_response_401.is_redirect = False
        mock_response_401.status_code = 401
        mock_response_401.json.return_value = {"statusCode": 401, "error": "Unauthorized", "message": "Invalid token",
                                               "attributes": {"error": "Invalid token"}}
        mock_response_401.return_value.text = '{"statusCode":401,"error":"Unauthorized","message":"Invalid token","attributes":{"error":"Invalid token"}}'

        mock_response_200 = Mock()
        mock_response_200.is_redirect = False
        mock_response_200.status_code = 200
        mock_response_200.return_value.text = json_response
        mock_response_200.json.return_value = json_response

        mock_auth = Mock()
        mock_session = Mock()
        mock_session.request.side_effect = [error.TokenExpiredError('Token Expired'),
                                            mock_response_401,
                                            mock_response_200]

        http_executor = http.HttpExecutor(mock_auth,
                                          session=mock_session,
                                          backoff_strategy={'interval': 0, 'max_tries': 2})
        response = http_executor.request("GET", "mock://test.com")

        assert_that(response.data, equal_to(json_response))

        call_list = [call('GET', 'mock://test.com', allow_redirects=False, data=None,
                          headers={'User-Agent': mock.ANY, 'Content-Type': 'application/vnd.piksel+json',
                                   'Accept': 'application/vnd.piksel+json', 'X-Correlation-ID': None}, params=None,
                          timeout=240),
                     call('GET', 'mock://test.com', allow_redirects=False, data=None,
                          headers={'User-Agent': mock.ANY, 'Content-Type': 'application/vnd.piksel+json',
                                   'Accept': 'application/vnd.piksel+json', 'X-Correlation-ID': None}, params=None,
                          timeout=240),
                     call('GET', 'mock://test.com', allow_redirects=False, data=None,
                          headers={'User-Agent': mock.ANY, 'Content-Type': 'application/vnd.piksel+json',
                                   'Accept': 'application/vnd.piksel+json', 'X-Correlation-ID': None}, params=None,
                          timeout=240)]

        assert_that(mock_session.request.call_count, is_(3))
        mock_session.request.assert_has_calls(call_list)

        assert_that(mock_session.auth.update_token.call_count, is_(2))

    def test_request_given_server_returns_an_token_expired_error_ever_then_the_request_should_fail(self):
        """
        Testing the max. number of retries when requesting new token and getting 401.
        """
        json_response = '{"resp2": "resp2"}'

        mock_response_401 = Mock()
        mock_response_401.is_redirect = False
        mock_response_401.status_code = 401
        mock_response_401.json.return_value = {"statusCode": 401, "error": "Unauthorized", "message": "Invalid token",
                                               "attributes": {"error": "Invalid token"}}
        mock_response_401.return_value.text = '{"statusCode":401,"error":"Unauthorized","message":"Invalid token","attributes":{"error":"Invalid token"}}'

        mock_auth = Mock()
        mock_session = Mock()
        mock_session.request.return_value = mock_response_401

        http_executor = http.HttpExecutor(mock_auth,
                                          session=mock_session,
                                          backoff_strategy={'interval': 0, 'max_tries': 2})

        with pytest.raises(error.HttpError):
            http_executor.request("GET", "mock://test.com")

        single_call = call('GET', 'mock://test.com', allow_redirects=False, data=None,
                           headers={'User-Agent': mock.ANY, 'Content-Type': 'application/vnd.piksel+json',
                                    'Accept': 'application/vnd.piksel+json', 'X-Correlation-ID': None},
                           params=None,
                           timeout=240)

        call_list = [single_call, single_call, single_call, single_call]

        mock_session.request.assert_has_calls(call_list)

    def test_request_given_server_returns_an_authorisation_error_fetching_the_token_then_error_is_not_retried(self):

        mock_auth = Mock()
        mock_session = Mock()
        mock_session.request.side_effect = error.AuthorisationError('Auth error')

        http_executor = http.HttpExecutor(mock_auth,
                                          session=mock_session,
                                          backoff_strategy={'interval': 0, 'max_tries': 3})

        with pytest.raises(error.AuthorisationError):
            http_executor.request("GET", "mock://test.com")

        mock_session.request.assert_called_once_with('GET', 'mock://test.com', allow_redirects=False, data=None,
                                                     headers={
                                                         'User-Agent': mock.ANY,
                                                         'Content-Type': 'application/vnd.piksel+json',
                                                         'Accept': 'application/vnd.piksel+json',
                                                         'X-Correlation-ID': None}, params=None, timeout=240)

    def test_request_given_server_returns_an_authorisation_error_then_fetch_token_does_not_count_as_retry(self):

        json_response = 'Error getting resource'

        mock_auth = Mock()
        mock_session = Mock()
        mock_session.request.side_effect = [error.AuthorisationError('Auth error'),
                                            {'text': json_response, 'status_code': 500},
                                            {'text': json_response, 'status_code': 200}]

        http_executor = http.HttpExecutor(mock_auth,
                                          session=mock_session,
                                          backoff_strategy={'interval': 0, 'max_tries': 1})

        with pytest.raises(error.AuthorisationError) as e:
            http_executor.request("GET", "mock://test.com")

        assert_that(e.value.args[0], is_('Auth error'))

        mock_session.request.assert_called_once_with('GET', 'mock://test.com', allow_redirects=False, data=None,
                                                     headers={
                                                         'User-Agent': mock.ANY,
                                                         'Content-Type': 'application/vnd.piksel+json',
                                                         'Accept': 'application/vnd.piksel+json',
                                                         'X-Correlation-ID': None}, params=None, timeout=240)

    def test_request_given_byo_type_and_server_returns_an_authorisation_error_then_error_is_propagated(self):
        json_response = '{"resp2": "resp2"}'

        self.adapter.register_uri('GET', 'mock://test.com', [{'text': 'resp1', 'status_code': 401},
                                                             {'text': json_response, 'status_code': 200}])

        http_executor = http.HttpExecutor(auth.AuthFactory.create(auth_type=auth.AuthType.BYO_TOKEN, byo_token='asdf'),
                                          session=self.session_mock,
                                          backoff_strategy={'interval': 0, 'max_tries': 1})
        with pytest.raises(error.HttpError) as e:
            http_executor.request("GET", "mock://test.com")

        assert_that(e.value.args[0], is_('An unexpected error occurred. HTTP Status code: 401.'
                                         ' Error message: Expecting value: line 1 column 1 (char 0). '))

    def test_request_given_a_resource_name_for_a_request_then_it_should_be_returned_with_the_request_result(self):
        self.adapter.register_uri('GET', 'mock://test.com', status_code=200)

        http_executor = http.HttpExecutor(auth.AuthFactory.create(grant_client_id="client_id",
                                                                  grant_client_secret="client_secret"),
                                          session=self.session_mock)

        resource_name_expected = 'resource_name_test'
        response = http_executor.request("GET", "mock://test.com", resource_name=resource_name_expected)

        assert_that(response.resource_name, equal_to(resource_name_expected))

    def test_given_none_content_type_property_then_header_should_contain_none_content_type(self):
        http_executor = http.HttpExecutor(None, content_type=None)
        assert_that(http_executor.common_headers['Content-Type'], is_('application/vnd.piksel+json'))
        assert_that(http_executor.common_headers['Accept'], is_('application/vnd.piksel+json'))

    def test_given_a_content_type_property_then_header_should_contain_that_content_type(self):
        http_executor = http.HttpExecutor(None, content_type='abc')
        assert_that(http_executor.common_headers['Content-Type'], is_('abc'))
        assert_that(http_executor.common_headers['Accept'], is_('abc'))

    def test_retries_for_http_status_code_specified_in_backoff_strategy_reach_default_limit(self):
        def _patch_max_time_to_run_unit_test_faster():
            import sequoia
            sequoia.http.HttpExecutor.MAX_TIME_SECONDS = 0.5

        json_response_404 = {'statusCode': 404, 'error': 'Not Found', 'message': 'Not Found'}
        mock_http_response_list = [{'json': json_response_404, 'status_code': 404}]

        _patch_max_time_to_run_unit_test_faster()
        self.adapter.register_uri(method='GET',
                                  url='mock://test.com',
                                  response_list=mock_http_response_list)
        http_executor = http.HttpExecutor(auth.AuthFactory.create(auth_type=auth.AuthType.BYO_TOKEN, byo_token='tkn'),
                                          session=self.session_mock,
                                          backoff_strategy={'max_tries': None,
                                                            'max_time': None,
                                                            'retry_http_status_codes': 404}
                                          )
        with pytest.raises(error.HttpError) as e:
            http_executor.request("GET", "mock://test.com")

        assert_that(e.value.status_code, is_(404))
        assert_that(self.adapter.called, is_(True))
        assert_that(self.adapter.called_once, is_(False))

    def test_retries_for_http_status_code_specified_in_backoff_strategy_with_number(self):
        json_response_404 = {'statusCode': 404, 'error': 'Not Found', 'message': 'Not Found'}
        json_response_200 = {'resources': [{'message': 'Found'}]}
        http_response_list = [
            {'json': json_response_404, 'status_code': 404},
            {'json': json_response_200, 'status_code': 200}
        ]
        self.backoff_test(mock_http_response_list=http_response_list,
                          max_tries=2,
                          retry_http_codes='404',
                          expected_http_status_code=200,
                          expected_json_response=json_response_200,
                          expected_requests_number=2)

    def test_retries_for_http_status_code_specified_in_backoff_strategy_with_list(self):
        json_response_404 = {'statusCode': 404, 'error': 'Not Found', 'message': 'Not Found'}
        json_response_409 = {'statusCode': 409, 'error': 'Conflict', 'message': 'Conflict'}
        json_response_200 = {'resources': [{'message': 'Found'}]}
        http_response_list = [
            {'json': json_response_404, 'status_code': 404},
            {'json': json_response_409, 'status_code': 409},
            {'json': json_response_200, 'status_code': 200}
        ]
        self.backoff_test(mock_http_response_list=http_response_list,
                          max_tries=4,
                          retry_http_codes=['404', 409, 410],
                          expected_http_status_code=200,
                          expected_json_response=json_response_200,
                          expected_requests_number=3)

    def test_retries_for_http_status_code_specified_in_backoff_strategy_with_tuple(self):
        json_response_404 = {'statusCode': 404, 'error': 'Not Found', 'message': 'Not Found'}
        json_response_409 = {'statusCode': 409, 'error': 'Conflict', 'message': 'Conflict'}
        json_response_200 = {'resources': [{'message': 'Found'}]}
        http_response_list = [
            {'json': json_response_404, 'status_code': 404},
            {'json': json_response_409, 'status_code': 409},
            {'json': json_response_200, 'status_code': 200}
        ]
        self.backoff_test(mock_http_response_list=http_response_list,
                          max_tries=4,
                          retry_http_codes=(404, '409', 410),
                          expected_http_status_code=200,
                          expected_json_response=json_response_200,
                          expected_requests_number=3)

    def backoff_test(self, mock_http_response_list, max_tries, retry_http_codes,
                     expected_http_status_code, expected_json_response, expected_requests_number):
        self.adapter.register_uri(method='GET',
                                  url='mock://test.com',
                                  response_list=mock_http_response_list)
        http_executor = http.HttpExecutor(auth.AuthFactory.create(auth_type=auth.AuthType.BYO_TOKEN, byo_token='tkn'),
                                          session=self.session_mock,
                                          user_agent='backoff_test',
                                          backoff_strategy={'max_tries': max_tries,
                                                            'max_time': 300,
                                                            'interval': 0,
                                                            'retry_http_status_codes': retry_http_codes
                                                            }
                                          )
        actual_response = http_executor.request("GET", "mock://test.com")
        assert_that(actual_response.status, is_(expected_http_status_code))
        assert_that(actual_response.data, equal_to(expected_json_response))
        assert_that(self.adapter.call_count, is_(expected_requests_number))
        for i in range(expected_requests_number): assert_that(self.adapter.request_history[i].method, is_('GET')) and \
                                                  assert_that(self.adapter.request_history[i].url, is_('mock://test.com'))

    def test_retries_when_main_resource_is_empty(self):
        """
        As the main resource is empty, the query is retried until it reached the limit of retries, then the latest
        http response is returned.
        """
        json_response_empty_contents = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [],
            "linked": {
                "assets": [
                    {"ref": "test:asset-1", "title": "asset 1"}
                ],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        http_response_list = [
            {'json': json_response_empty_contents, 'status_code': 200}
        ]
        expected_requests_test_1 = 5
        expected_requests_test_2 = 5
        expected_requests_test_3 = 2

        def backoff_as_dict(expected_requests_test_1, http_response_list, json_response_empty_contents):
            self.retry_when_empty_result_test(
                mock_http_response_list=http_response_list,
                backoff_strategy_constructor={'max_tries': 5, 'interval': 0, 'retry_when_empty_result':{'contents': True}},
                backoff_strategy_request=None,
                retry_when_empty_result=None,
                expected_http_status_code=200,
                expected_json_response=json_response_empty_contents,
                expected_requests_number=expected_requests_test_1)

        def backoff_as_boolean(expected_requests_test_1, expected_requests_test_2, http_response_list,
                               json_response_empty_contents):
            self.retry_when_empty_result_test(
                mock_http_response_list=http_response_list,
                backoff_strategy_constructor={'max_tries': 5, 'interval': 0, 'retry_when_empty_result': True},
                backoff_strategy_request=None,
                retry_when_empty_result=None,
                expected_http_status_code=200,
                expected_json_response=json_response_empty_contents,
                expected_requests_number=expected_requests_test_1 + expected_requests_test_2)

        def backoff_in_method_precedes_constructor(expected_requests_test_1, expected_requests_test_2,
                                                   expected_requests_test_3, http_response_list,
                                                   json_response_empty_contents):
            self.retry_when_empty_result_test(
                mock_http_response_list=http_response_list,
                backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
                backoff_strategy_request={'max_tries': expected_requests_test_3, 'interval': 0, 'retry_when_empty_result': True},
                retry_when_empty_result=None,
                expected_http_status_code=200,
                expected_json_response=json_response_empty_contents,
                expected_requests_number=expected_requests_test_1 + expected_requests_test_2 + expected_requests_test_3)

        backoff_as_dict(expected_requests_test_1, http_response_list, json_response_empty_contents)
        backoff_as_boolean(expected_requests_test_1, expected_requests_test_2, http_response_list,
                           json_response_empty_contents)
        backoff_in_method_precedes_constructor(expected_requests_test_1, expected_requests_test_2,
                                               expected_requests_test_3, http_response_list,
                                               json_response_empty_contents)

    def test_retries_when_main_resource_is_empty_and_eventually_it_is_not(self):
        """
        As the main resource is empty for the first queries, the query is retried until the main resource is not empty
        anymore in the response, then the response is returned.
        """
        json_response_200_empty = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [],
            "linked": {
                "assets": [
                    {"ref": "test:asset-1", "title": "asset 1"}
                ],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        json_response_200 = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [
                {"ref": "test:c0007", "owner": "test", "name": "c0007", "title": "Interstellar",
                 "categoryRefs": ["test:category-1", "test:category-2"]}
            ],
            "linked": {
                "assets": [
                    {"ref": "test:asset-1", "title": "asset 1"}
                ],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        http_response_list = [
            {'json': json_response_200_empty, 'status_code': 200},
            {'json': json_response_200_empty, 'status_code': 200},
            {'json': json_response_200, 'status_code': 200}
        ]
        expected_requests_test_1 = 3
        expected_requests_test_2 = 3
        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0, 'retry_when_empty_result': {'contents': True}},
            backoff_strategy_request=None,
            retry_when_empty_result=None,
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1)

        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0, 'retry_when_empty_result': True},
            backoff_strategy_request=None,
            retry_when_empty_result=None,
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1 + expected_requests_test_2)

    def test_retries_when_include_resource_is_empty(self):
        """
        As assets is empty in the response the query is retried, when the limit of retries is reached the latest
        http response is returned
        """
        json_response_200 = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [
                {"ref": "test:c0007", "owner": "test", "name": "c0007", "title": "Interstellar",
                 "categoryRefs": ["test:category-1", "test:category-2"]}
            ],
            "linked": {
                "assets": [],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        http_response_list = [
            {'json': json_response_200, 'status_code': 200}
        ]
        expected_requests_test_1 = 5
        expected_requests_test_2 = 5
        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0, 'retry_when_empty_result': {'contents': True, 'assets': True, 'categories': True}},
            backoff_strategy_request=None,
            retry_when_empty_result=None,
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1)

        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0, 'retry_when_empty_result': True},
            backoff_strategy_request=None,
            retry_when_empty_result=None,
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1 + expected_requests_test_2)

    def test_retries_when_include_resource_is_empty_but_not_required(self):
        """
        Although assets is empty in the response the query is not retried because assets is not required in the
        param retry_when_empty_result
        """
        json_response_200 = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [
                {"ref": "test:c0007", "owner": "test", "name": "c0007", "title": "Interstellar",
                 "categoryRefs": ["test:category-1", "test:category-2"]}
            ],
            "linked": {
                "assets": [],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        http_response_list = [
            {'json': json_response_200, 'status_code': 200}
        ]
        expected_requests_test_1 = 1
        expected_requests_test_2 = 1
        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0, 'retry_when_empty_result': {'contents': True, 'assets': False, 'categories': True}},
            backoff_strategy_request=None,
            retry_when_empty_result=None,
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1)

        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0, 'retry_when_empty_result': {'contents': True, 'categories': True}},
            backoff_strategy_request=None,
            retry_when_empty_result=None,
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1 + expected_requests_test_2)

    def test_retries_when_main_resource_is_empty_using_deprecated_argument(self):
        """
        As the main resource is empty, the query is retried until it reached the limit of retries, then the latest
        http response is returned.
        """
        json_response_empty_contents = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [],
            "linked": {
                "assets": [
                    {"ref": "test:asset-1", "title": "asset 1"}
                ],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        http_response_list = [
            {'json': json_response_empty_contents, 'status_code': 200}
        ]
        expected_requests_test_1 = 5
        expected_requests_test_2 = 5
        expected_requests_test_3 = 2

        def backoff_as_dict(expected_requests_test_1, http_response_list, json_response_empty_contents):
            self.retry_when_empty_result_test(
                mock_http_response_list=http_response_list,
                backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
                backoff_strategy_request=None,
                retry_when_empty_result={'contents': True},
                expected_http_status_code=200,
                expected_json_response=json_response_empty_contents,
                expected_requests_number=expected_requests_test_1)

        def backoff_as_boolean(expected_requests_test_1, expected_requests_test_2, http_response_list,
                               json_response_empty_contents):
            self.retry_when_empty_result_test(
                mock_http_response_list=http_response_list,
                backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
                backoff_strategy_request=None,
                retry_when_empty_result=True,
                expected_http_status_code=200,
                expected_json_response=json_response_empty_contents,
                expected_requests_number=expected_requests_test_1 + expected_requests_test_2)


        def backoff_in_method_precedes_constructor(expected_requests_test_1, expected_requests_test_2,
                                                   expected_requests_test_3, http_response_list,
                                                   json_response_empty_contents):
            self.retry_when_empty_result_test(
                mock_http_response_list=http_response_list,
                backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
                backoff_strategy_request={'max_tries': expected_requests_test_3, 'interval': 0},
                retry_when_empty_result=True,
                expected_http_status_code=200,
                expected_json_response=json_response_empty_contents,
                expected_requests_number=expected_requests_test_1 + expected_requests_test_2 + expected_requests_test_3)

        backoff_as_dict(expected_requests_test_1, http_response_list, json_response_empty_contents)
        backoff_as_boolean(expected_requests_test_1, expected_requests_test_2, http_response_list,
                           json_response_empty_contents)
        backoff_in_method_precedes_constructor(expected_requests_test_1, expected_requests_test_2,
                                               expected_requests_test_3, http_response_list,
                                               json_response_empty_contents)

    def test_retries_when_main_resource_is_empty_and_eventually_it_is_not_using_deprecated_argument(self):
        """
        As the main resource is empty for the first queries, the query is retried until the main resource is not empty
        anymore in the response, then the response is returned.
        """
        json_response_200_empty = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [],
            "linked": {
                "assets": [
                    {"ref": "test:asset-1", "title": "asset 1"}
                ],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        json_response_200 = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [
                {"ref": "test:c0007", "owner": "test", "name": "c0007", "title": "Interstellar",
                 "categoryRefs": ["test:category-1", "test:category-2"]}
            ],
            "linked": {
                "assets": [
                    {"ref": "test:asset-1", "title": "asset 1"}
                ],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        http_response_list = [
            {'json': json_response_200_empty, 'status_code': 200},
            {'json': json_response_200_empty, 'status_code': 200},
            {'json': json_response_200, 'status_code': 200}
        ]
        expected_requests_test_1 = 3
        expected_requests_test_2 = 3
        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
            backoff_strategy_request=None,
            retry_when_empty_result={'contents': True},
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1)

        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
            backoff_strategy_request=None,
            retry_when_empty_result=True,
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1 + expected_requests_test_2)

    def test_retries_when_include_resource_is_empty_using_deprecated_argument(self):
        """
        As assets is empty in the response the query is retried, when the limit of retries is reached the latest
        http response is returned
        """
        json_response_200 = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [
                {"ref": "test:c0007", "owner": "test", "name": "c0007", "title": "Interstellar",
                 "categoryRefs": ["test:category-1", "test:category-2"]}
            ],
            "linked": {
                "assets": [],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        http_response_list = [
            {'json': json_response_200, 'status_code': 200}
        ]
        expected_requests_test_1 = 5
        expected_requests_test_2 = 5
        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
            backoff_strategy_request=None,
            retry_when_empty_result={'contents': True, 'assets': True, 'categories': True},
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1)

        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
            backoff_strategy_request=None,
            retry_when_empty_result=True,
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1 + expected_requests_test_2)

    def test_retries_when_include_resource_is_empty_but_not_required_using_deprecated_argument(self):
        """
        Although assets is empty in the response the query is not retried because assets is not required in the
        param retry_when_empty_result
        """
        json_response_200 = {
            "meta": {
                "perPage": 100, "page": 1,
                "first": "/data/contents?include=assets%2Ccategories&owner=test&withRef=test%3Ac0007&page=1&perPage=100",
                "linked": {
                    "assets": [{"perPage": 100,
                                "request": "/data/assets?owner=test&fields=ref%2Cname%2CcontentRef%2Ctype%2Curl%2CfileFormat%2Ctitle%2CfileSize%2Ctags&continue=true&withContentRef=test%3Ac0007"}],
                    "categories": [{"perPage": 100, "page": 1,
                                    "first": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2&page=1&perPage=100",
                                    "request": "/data/categories?owner=test&withRef=test%3Acategory-1%7C%7Ctest%3Acategory-2"}
                                   ]}},
            "contents": [
                {"ref": "test:c0007", "owner": "test", "name": "c0007", "title": "Interstellar",
                 "categoryRefs": ["test:category-1", "test:category-2"]}
            ],
            "linked": {
                "assets": [],
                "categories": [
                    {"ref": "test:category-1", "title": "a tag category", "scheme": "tags", "value": "tag"},
                    {"ref": "test:category-2", "title": "a tag category", "scheme": "tags", "value": "tag"}
                ]}}
        http_response_list = [
            {'json': json_response_200, 'status_code': 200}
        ]
        expected_requests_test_1 = 1
        expected_requests_test_2 = 1
        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
            backoff_strategy_request=None,
            retry_when_empty_result={'contents': True, 'assets': False, 'categories': True},
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1)

        self.retry_when_empty_result_test(
            mock_http_response_list=http_response_list,
            backoff_strategy_constructor={'max_tries': 5, 'interval': 0},
            backoff_strategy_request=None,
            retry_when_empty_result={'contents': True, 'categories': True},
            expected_http_status_code=200,
            expected_json_response=json_response_200,
            expected_requests_number=expected_requests_test_1 + expected_requests_test_2)

    def retry_when_empty_result_test(self, mock_http_response_list,
                                     backoff_strategy_constructor, backoff_strategy_request, retry_when_empty_result,
                                     expected_http_status_code, expected_json_response, expected_requests_number):
        self.adapter.register_uri(
            method='GET',
            url='mock://metadata.pikselpalette.com/data/contents?include=assets,categories&owner=test&withRef=test:c0007',
            response_list=mock_http_response_list)
        http_executor = http.HttpExecutor(
            auth.AuthFactory.create(auth_type=auth.AuthType.BYO_TOKEN, byo_token='tkn'),
            session=self.session_mock,
            user_agent='backoff_test',
            backoff_strategy=backoff_strategy_constructor)
        actual_response = http_executor.request(
            method="GET",
            url="mock://metadata.pikselpalette.com/data/contents?include=assets,categories&owner=test&withRef=test:c0007",
            resource_name='contents',
            backoff_strategy=backoff_strategy_request,
            retry_when_empty_result=retry_when_empty_result
        )
        assert_that(actual_response.status, is_(expected_http_status_code))
        assert_that(actual_response.data, equal_to(expected_json_response))
        assert_that(self.adapter.call_count, is_(expected_requests_number))
        for i in range(expected_requests_number):
            assert_that(self.adapter.request_history[i].method, is_('GET'))
            assert_that(self.adapter.request_history[i].url, is_('mock://metadata.pikselpalette.com/data/contents?include=assets,categories&owner=test&withRef=test:c0007'))

    def test_given_backoff_strategy_at_method_level_has_priority_over_constructor_level(self):
        # Prepare test
        backoff_constructor_level = {
            'max_tries': 6,
            'interval': 0
        }
        backoff_method_level = {
            'max_tries': 4,
            'interval': 0,
            'retry_http_status_codes': 404
        }
        json_response_found = {'resources': [{'message': 'Found'}]}
        self.adapter.register_uri(
            method='GET',
            url='mock://metadata.pikselpalette.com/data/contents?include=assets&owner=test&withRef=test:c0007',
            response_list=[
                {'json': {'statusCode': 404, 'error': 'Not Found', 'message': 'Not Found'}, 'status_code': 404},
                {'json': {'statusCode': 404, 'error': 'Not Found', 'message': 'Not Found'}, 'status_code': 404},
                {'json': json_response_found, 'status_code': 200}
            ])
        self.adapter.register_uri(
            method='GET',
            url='mock://metadata.pikselpalette.com/data/contents?include=assets&owner=test&withRef=test:a',
            response_list=[
                {'json': {'statusCode': 404, 'error': 'Not Found', 'message': 'Not Found'}, 'status_code': 404}
            ])

        # Create the http_executor object
        http_executor = http.HttpExecutor(
            auth.AuthFactory.create(auth_type=auth.AuthType.BYO_TOKEN, byo_token='tkn'),
            session=self.session_mock,
            user_agent='backoff_test',
            backoff_strategy=backoff_constructor_level)

        # First request using a custom backoff_strategy
        actual_response = http_executor.request(
            method="GET",
            url="mock://metadata.pikselpalette.com/data/contents?include=assets&owner=test&withRef=test:c0007",
            resource_name='contents',
            backoff_strategy=backoff_method_level
        )

        first_request_retries = 3
        assert_that(actual_response.status, is_(200))
        assert_that(actual_response.data, equal_to(json_response_found))
        assert_that(self.adapter.call_count, is_(first_request_retries))
        for i in range(first_request_retries):
            assert_that(self.adapter.request_history[i].method, is_('GET'))
            assert_that(self.adapter.request_history[i].url, is_('mock://metadata.pikselpalette.com/data/contents?include=assets&owner=test&withRef=test:c0007'))

        # Second request using the constructor backoff_strategy
        with pytest.raises(error.HttpError) as sequoia_error:
            http_executor.request(
                method="GET",
                url="mock://metadata.pikselpalette.com/data/contents?include=assets&owner=test&withRef=test:a",
                resource_name='contents'
            )

        second_request_retries = 1
        assert_that(sequoia_error.value.status_code, is_(404))
        assert_that(sequoia_error.value.message, is_({'statusCode': 404, 'error': 'Not Found', 'message': 'Not Found'}))
        assert_that(sequoia_error.value.cause, none())
        assert_that(self.adapter.call_count, is_(first_request_retries + second_request_retries))
