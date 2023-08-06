import logging
import os
import uuid
from time import sleep

import pytest
from hamcrest import assert_that, has_length, is_, none

from sequoia import auth, criteria
from sequoia.client import Client
from sequoia.error import HttpError, NotMatchingVersion
from tests import mocking
from tests.common import TestGeneric

# This is to allow us to test without requiring a https transport
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Mark the test to be ran as part of the local integration testing
pytestmark = pytest.mark.integration_test


class TestEndpointProxy(TestGeneric):

    def setUp(self):
        super().setUp()
        self.owner = 'testmock'
        self.registry = 'https://registry.sandbox.eu-west-1.palettedev.aws.pikselpalette.com/services/testmock'

    def test_can_post_and_retrieve_json_payload(self):
        random_name = 'aSampleProfile-' + str(uuid.uuid4())
        profile = profile_template % random_name

        client = Client(self.registry,
                        user_id='     the_user_id',
                        application_id='the_application_id ',
                        correlation_id='                ',
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        profile_endpoint = client.flow.profiles
        store_result = profile_endpoint.store(self.owner, profile)
        read_result = profile_endpoint.read(self.owner, store_result.resources[0]['ref'])
        delete_result = profile_endpoint.delete(self.owner, store_result.resources[0]['ref'])

        assert_that(store_result.status, 201)
        assert_that(delete_result.status, 204)
        assert_that(read_result.resources[0]['name'], random_name)

        read_result_object = read_result.to_object()
        assert_that(read_result_object[0].name, random_name)
        assert_that(read_result_object[0].secrets.awsKey1, 'awsKeyValue1')
        assert_that(read_result_object[0].secrets.ftpKey1, 'ftpKeyValue1')

    def test_can_post_and_retrieve_linked_content(self):

        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password, model_resolution='direct')
        contents_endpoint = client.metadata.contents
        categories_endpoint = client.metadata.categories
        store_content = None
        store_category = None
        try:

            store_content = contents_endpoint.store(self.owner, content_with_category_template)
            store_category = categories_endpoint.store(self.owner, category_template)
            sleep(1)
            result = contents_endpoint.browse(self.owner, criteria.Criteria().add(
                inclusion=criteria.Inclusion.resource('categories')).add(
                criterion=criteria.StringExpressionFactory.field('ref').equal_to(
                    store_content.resources[0]['ref'])))
        finally:
            if store_content:
                delete_result = contents_endpoint.delete(self.owner, store_content.resources[0]['ref'])
            if store_category:
                delete_result = categories_endpoint.delete(self.owner, store_category.resources[0]['ref'])

        assert_that(result.model, has_length(1))
        assert_that(result.status, 201)
        assert_that(result.model[0]['name'], 'a_test_content_linked_to_categories')
        assert_that(result.model[0]['categories'], has_length(1))
        assert_that(result.model[0]['categories'][0]['ref'], 'testmock:genre_animation')

    def test_can_delete_and_manage_empty_payload(self):
        random_name = 'aSampleProfile-' + str(uuid.uuid4())
        profile = profile_template % random_name

        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        profile_endpoint = client.flow.profiles
        store_result = profile_endpoint.store(self.owner, profile)
        read_result = profile_endpoint.read(self.owner, store_result.resources[0]['ref'])
        delete_result = profile_endpoint.delete(self.owner, store_result.resources[0]['ref'])

        assert_that(store_result.status, 201)
        assert_that(delete_result.status, 204)
        assert_that(delete_result.result, none())
        assert_that(read_result.resources[0]['name'], random_name)

    def test_given_assets_then_browse_with_content_ref_should_retrieve_assets(self):
        assets_ids, content_name = self._create_ids_and_content(5)
        content = content_template % content_name
        assets = assets_template % assets_ids
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        content_endpoint = client.metadata.contents
        assets_endpoint = client.metadata.assets
        content_endpoint.store(self.owner, content)
        assets_endpoint.store(self.owner, assets)
        sleep(1)
        response = assets_endpoint.browse(
            self.owner,
            criteria.Criteria().add(
                criterion=criteria.StringExpressionFactory.field("contentRef").equal_to(
                    'testmock:%s' % content_name)))
        assert_that(response.resources, has_length(5))
        # Clean up
        content_endpoint.delete(self.owner, 'testmock:' + content_name)
        for name in assets_ids:
            assets_endpoint.delete(self.owner, 'testmock:' + name)

    def test_given_assets_then_browse_with_query_string_should_retrieve_assets(self):
        assets_ids, content_name = self._create_ids_and_content(5)
        content = content_template % content_name
        assets = assets_template % assets_ids
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        content_endpoint = client.metadata.contents
        assets_endpoint = client.metadata.assets
        content_endpoint.store(self.owner, content)
        assets_endpoint.store(self.owner, assets)
        sleep(1)
        response = assets_endpoint.browse(self.owner, query_string='withContentRef=testmock:%s' % content_name)
        assert_that(response.resources, has_length(5))
        # Clean up
        content_endpoint.delete(self.owner, 'testmock:' + content_name)
        for name in assets_ids:
            assets_endpoint.delete(self.owner, 'testmock:' + name)

    def test_given_assets_with_pagination_then(self):
        assets_ids, content_name = self._create_ids_and_content(5)
        content = content_template % content_name
        assets = assets_template % assets_ids
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        content_endpoint = client.metadata.contents
        assets_endpoint = client.metadata.assets
        content_endpoint.store(self.owner, content)
        assets_endpoint.store(self.owner, assets)

        # Getting content stored previously, sometimes is empty
        sleep(3)

        query_string = 'perPage=2&withContentRef=testmock:%s' % content_name
        content_pages = [response for response in assets_endpoint.browse(self.owner, query_string=query_string)]

        assert_that(content_pages[0].resources, has_length(2))
        assert_that(content_pages[1].resources, has_length(2))
        assert_that(content_pages[2].resources, has_length(1))
        # Clean up
        content_endpoint.delete(self.owner, 'testmock:' + content_name)
        for name in assets_ids:
            assets_endpoint.delete(self.owner, 'testmock:' + name)

    def _create_ids_and_content(self, ids_number):
        content_name = str(uuid.uuid4())
        assets_tuple = zip(tuple(str(uuid.uuid4()) for i in range(0, ids_number)), [content_name] * ids_number)
        assets_flatted_tuple = tuple([element for tupl in assets_tuple for element in tupl])

        return assets_flatted_tuple, content_name

    def test_given_no_assets_then_browse_with_content_ref_should_not_retrieve_assets(self):
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        assets_endpoint = client.metadata.assets

        response = assets_endpoint.browse(
            self.owner,
            criteria.Criteria().add(
                criterion=criteria.StringExpressionFactory.field('contentRef').equal_to(
                    'testmock:nonExistingContent')))

        assert len(response.resources) == 0

    def test_given_assets_with_errors_then_store_should_raise_an_error(self):
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        assets_endpoint = client.metadata.assets
        with pytest.raises(HttpError):
            assets_endpoint.store(self.owner, assets_with_errors)

    def test_given_asset_with_different_version_then_update_should_raise_an_error(self):
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        assets_endpoint = client.metadata.assets
        assets_endpoint.store(self.owner, asset_to_store)
        with pytest.raises(NotMatchingVersion) as e:
            assets_endpoint.update(self.owner, asset, 'testmock:016b9e5f-c184-48ea-a5e2-6e6bc2d62791',
                                   'e3706cb187f8decf810f8a3645c4e178aa65b0d1')

        assert e.value.message == 'Document cannot be updated. Version does not match.'

    def test_given_wrong_registry_url_should_raise_an_error(self):
        with pytest.raises(HttpError) as e:
            Client('https://registry.sandbox.eu-west-1.palettedev.aws.pikselpalette.com/service/testmock',
                   grant_client_id=self.config.ingest.username,
                   grant_client_secret=self.config.ingest.password)

        assert e.value.message['statusCode'] == 404

    def test_given_http_registry_url_should_redirect(self):
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        assert client._registry

    def test_flow_execution_progress_business_endpoint_when_flow_execution_not_found_raise_an_error(self):
        ref = 'flow-execution-that-not-exists'
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)

        with pytest.raises(HttpError) as e:
            client.flow.business('/$service/$owner:$ref').browse(service='execution-progress',
                                                                     owner=self.owner, ref=ref)
        assert_that(e.value.status_code, is_(404))

    def test_validation_business_endpoint_without_authentication_when_rule_not_exists_raise_error(self):
        rule = 'rule-not-exists'

        client = Client('http://registry.sandbox.eu-west-1.palettedev.aws.pikselpalette.com/services/testmock',
                        auth_type=auth.AuthType.NO_AUTH)

        with pytest.raises(HttpError):
            client.validation.business('/$service/$owner/$ref').browse(service='v', owner='test',
                                                                       content=content_to_validate,
                                                                       ref=rule)

    def test_given_assets_with_pagination_then_linked_links_are_paginated(self):
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)

        content_name = str(uuid.uuid4())

        assets_ids_1 = self._create_ids_and_content_for_pagination_of_linked(99, content_name)
        assets_ids_2 = self._create_ids_and_content_for_pagination_of_linked(99, content_name)
        assets_ids_3 = self._create_ids_and_content_for_pagination_of_linked(99, content_name)
        assets_ids_4 = self._create_ids_and_content_for_pagination_of_linked(99, content_name)
        assets_ids_5 = self._create_ids_and_content_for_pagination_of_linked(99, content_name)
        assets_ids_6 = self._create_ids_and_content_for_pagination_of_linked(99, content_name)
        content = content_template % content_name
        with open(mocking.__location__ + '/test_files/assets_99_items_template.json') as file:
            assets_template_linked = file.read()

        assets_1 = assets_template_linked % assets_ids_1
        assets_2 = assets_template_linked % assets_ids_2
        assets_3 = assets_template_linked % assets_ids_3
        assets_4 = assets_template_linked % assets_ids_4
        assets_5 = assets_template_linked % assets_ids_5
        assets_6 = assets_template_linked % assets_ids_6

        content_endpoint = client.metadata.contents
        assets_endpoint = client.metadata.assets

        content_endpoint.store(self.owner, content)
        assets_endpoint.store(self.owner, assets_1)
        assets_endpoint.store(self.owner, assets_2)
        assets_endpoint.store(self.owner, assets_3)
        assets_endpoint.store(self.owner, assets_4)
        assets_endpoint.store(self.owner, assets_5)
        assets_endpoint.store(self.owner, assets_6)

        # Getting content stored previously, sometimes is empty
        sleep(3)

        query_string = 'include=assets&withRef=' + 'testmock:' + content_name

        contents_response = content_endpoint.browse(self.owner, query_string=query_string)

        asset_linked = contents_response.linked('assets')
        asset_linked = contents_response.linked('assets')

        assert_that(contents_response.resources, has_length(1))
        assert_that(len(asset_linked.resources), is_(500))

        asset_pages = [page for page in asset_linked]
        assert_that(len(asset_pages[0]), is_(500))
        assert_that(len(asset_pages[1]), is_(94))

        # Clean up
        content_endpoint.delete(self.owner, 'testmock:' + content_name)
        asset_ids = assets_ids_1 + assets_ids_2 + assets_ids_3 + assets_ids_4 + assets_ids_5 + assets_ids_6
        refs = "testmock:" + ",testmock:".join(asset_ids)
        l_refs = refs.split(",")
        max_size_each_sublist = 119
        splits = [l_refs[x:x+max_size_each_sublist] for x in range(0, len(l_refs), max_size_each_sublist)]
        for split in splits:
            assets_endpoint.delete(self.owner, split)

    def test_refresh_sequoia_token(self):
        """
        When you perform a query against Sequoia and your token has expired or it's been invalidated,
        a new token is taken and used to perform your query.
        """
        assets_ids, content_name = self._create_ids_and_content(5)
        content = content_template % content_name
        assets = assets_template % assets_ids
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password)
        content_endpoint = client.metadata.contents
        assets_endpoint = client.metadata.assets
        content_endpoint.store(self.owner, content)
        assets_endpoint.store(self.owner, assets)
        sleep(1)
        response = assets_endpoint.browse(
            self.owner,
            criteria.Criteria().add(
                criterion=criteria.StringExpressionFactory.field("contentRef").equal_to(
                    'testmock:%s' % content_name)))
        assert_that(response.resources, has_length(5))

        # Revoke the token (not using clientsdk)
        token_previous = client._auth.session.access_token
        import base64, requests
        my_auth_creds = base64.b64encode('{}:{}'.format(self.config.sequoia.username, self.config.sequoia.password).encode('ascii')).decode('ascii')
        url = "https://identity.sandbox.eu-west-1.palettedev.aws.pikselpalette.com/oauth/revoke"
        payload = 'token=' + token_previous
        headers = {
            'authorization': 'Basic ' + my_auth_creds,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        assert_that(response.status_code, is_(200))

        # Query again
        sleep(10)
        response = assets_endpoint.browse(
            self.owner,
            criteria.Criteria().add(
                criterion=criteria.StringExpressionFactory.field("contentRef").equal_to(
                    'testmock:%s' % content_name)))
        assert_that(response.resources, has_length(5))
        token_current = client._auth.session.access_token
        print('*********')
        print('TOKEN OLD (revoked): '+token_previous)
        print('TOKEN NEW (updated): ' + token_current)
        print('*********')
        # assert_that(token_previous, is_not(equal_to(token_current)))

        # Clean up
        content_endpoint.delete(self.owner, 'testmock:' + content_name)
        for name in assets_ids:
            assets_endpoint.delete(self.owner, 'testmock:' + name)

    def _create_ids_and_content_for_pagination_of_linked(self, ids_number, content_name):
        assets_tuple = zip(tuple(str(uuid.uuid4()) for i in range(0, ids_number)), [content_name] * ids_number)
        assets_flatted_tuple = tuple([element for tupl in assets_tuple for element in tupl])

        return assets_flatted_tuple

    def test_retry_when_empty_then_browse_with_content_ref_should_not_retrieve_assets(self):
        self._configure_logging()
        unique_name = str(uuid.uuid4())

        import backoff
        client = Client(self.registry,
                        grant_client_id=self.config.sequoia.username,
                        grant_client_secret=self.config.sequoia.password,
                        user_agent='backoff_test'
                        )
        contents_endpoint = client.metadata.contents
        categories_endpoint = client.metadata.categories

        content = content_template_unique % (unique_name, unique_name, unique_name)
        categories = category_template_unique % (unique_name, unique_name)

        contents_result = contents_endpoint.store(self.owner, content)
        categories_result = categories_endpoint.store(self.owner, categories)
        sleep(1)

        response = contents_endpoint.browse(
            self.owner,
            criteria.Criteria()
                .add_criterion(criteria.StringExpressionFactory.field('ref').equal_to(f'testmock:{unique_name}'))
                .add_inclusion(criteria.Inclusion.resource('categories'))
                .add_inclusion(criteria.Inclusion.resource('assets')),
            backoff_strategy={
                'wait_gen': backoff.expo,
                'max_tries': 3,
                # 'max_time': 10,
                'retry_http_status_codes': '404',
                'retry_when_empty_result': {
                    'contents': True,
                    'assets': True,
                    'categories': True
                }
            }
        )

        from pprint import pformat
        logging.info(pformat(response.resources))

        assert len(response.resources) == 1
        assert len(response.linked('categories').resources) == 2
        assert len(response.linked('assets').resources) == 0
        # This test returns the data it has found after retrying the query as there's no assets and they are required

        categories_endpoint.delete(self.owner, categories_result.resources[0]['ref'])
        categories_endpoint.delete(self.owner, categories_result.resources[1]['ref'])
        contents_endpoint.delete(self.owner, contents_result.resources[0]['ref'])

    def _configure_logging(self):
        import sys
        # formatter = logging.Formatter('[%(asctime)s] %(name)-12s [%(module)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')
        formatter = logging.Formatter('%(asctime)s - %(levelname)-6s - %(name)-12s - %(message)s')
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.DEBUG)
        console.setFormatter(formatter)
        file_handler = logging.FileHandler('sequoia.log')
        file_handler.setFormatter(formatter)
        logging.getLogger().addHandler(console)
        logging.getLogger().addHandler(file_handler)
        # root.addHandler(console)

        logging.getLogger().setLevel(logging.INFO)
        logging.getLogger('sequoia').setLevel(logging.DEBUG)
        logging.getLogger('sequoia.registry').setLevel(logging.INFO)
        logging.getLogger('backoff').setLevel('NOTSET')
        logging.getLogger('urllib3').setLevel(logging.WARN)
        logging.getLogger('requests_oauthlib').setLevel(logging.WARN)


rule_to_post = {
    "rules": [
        {
            "owner": "testmock",
            "name": "content-movie-validation",
            "title": "Validation Rules for Movies",
            "service": "metadata",
            "resource": "contents",
            "active": True,
            "facts": {"title": ['required', {'max_length': 20}]}
        }
    ]
}

content_to_validate = {"contents": [
    {
        "ref": "test:609dabcddc229f308f20d01a3d8ff68289950debc14d6ee2cf48e004474512fe",
        "alternativeIdentifiers": {
            "crid": "crid://virginmedia.com/content/MV010463750000"
        },
        "owner": "test",
        "name": "609dabcddc229f308f20d01a3d8ff68289950debc14d6ee2cf48e004474512fe",
        "title": "Naagin Bani Suhagan",
        "type": "movie",
        "sortTitle": "Naagin Bani Suhagan",
        "collateCharacter": "N",
        "mediumSynopsis": "A woman tries to get revenge on the man who murdered her husband.",
        "releaseYear": 2012,
        "active": True,
        "categoryRefs": [
            "demo:genre-9"
        ]
    },
    {
        "ref": "test:123",
        "owner": "test",
        "name": "123",
        "title": "Naagin Bani Suhagan",
        "type": "movie",
        "sortTitle": "Naagin Bani Suhagan",
        "collateCharacter": "N",
        "mediumSynopsis": "A woman tries to get revenge on the man who murdered her husband.",
        "releaseYear": 2012,
        "active": True,
        "categoryRefs": [
            "demo:genre-9"
        ]
    }
]
}

content_including_categories = """
    [
        {
            "owner": "testmock",
            "name": "a_test_content_linked_to_categories",
            "type": "episode"
            "cartegories" : {
                "name": "genre_animation",
                "title": "Animation",
                "scheme": "genre",
                "value": "Animation",
                "active": true
            }
        }
    ]
"""
category_template = """
[
    {
        "owner": "testmock",
        "name": "genre_animation",
        "title": "Animation",
        "scheme": "genre",
        "value": "Animation",
        "active": true
    }
]
"""

content_with_category_template = """
            [
                {
                    "owner": "testmock",
                    "name": "a_test_content_linked_to_categories",
                    "type": "episode",
                    "categoryRefs" : ["testmock:genre_animation"]
                }
            ]
    """

profile_template = """
          [
            {
              "owner": "testmock",
              "name": "%s",
              "secrets": {
                "awsKey1": "awsKeyValue1",
                "ftpKey1": "ftpKeyValue1"
              }
            }
          ]
    """

content_template_unique = """
[
    {
      "owner": "testmock",
      "name": "%s",
      "type": "movie",
      "title": "Interstellar",
      "longSynopsis": "Long synopsis for Interstellar...",
      "mediumSynopsis": "Medium synopsis for Interstellar...",
      "shortSynopsis": "Short synopsis for Interstellar...",
      "availabilityStartAt": "2016-04-01T12:00:00.000Z",
      "availabilityEndAt": "2016-07-01T12:00:00.000Z",
      "releaseYear": 2014,
      "duration": "PT1H20M",
      "ratings": {
        "BBFC": "PG"
      },
      "active": true,
      "categoryRefs": [
        "testmock:category-1-%s",
        "testmock:category-2-%s"
      ]
    }
  ]
"""

category_template_unique = """
[
    {
        "owner": "testmock",
        "name": "category-1-%s",
        "title": "Animation",
        "scheme": "genre",
        "value": "Animation",
        "active": true
    },
    {
        "owner": "testmock",
        "name": "category-2-%s",
        "title": "Animation",
        "scheme": "genre",
        "value": "Animation",
        "active": true
    }
]
"""

content_template = """
            [
                {
                    "owner": "testmock",
                    "name": "%s",
                    "type": "episode"
                }
            ]
    """

asset = """
    [
        {
            "owner": "testmock",
            "name": "016b9e5f-c184-48ea-a5e2-6e6bc2d62791",
            "ref": "testmock:016b9e5f-c184-48ea-a5e2-6e6bc2d62791",
            "title": "A very nice title",
            "tags": [
                "todo",
                "usage:boxart"
            ],
            "type": "video",
            "contentRef": "testmock:sampleContent",
            "active": true,
            "version":"e3706cb187f8decf810f8a3645c4e178aa65b0d1"
        }
    ]
"""

asset_to_store = """
    [
        {
            "owner": "testmock",
            "name": "016b9e5f-c184-48ea-a5e2-6e6bc2d62791",
            "ref": "testmock:016b9e5f-c184-48ea-a5e2-6e6bc2d62791",
            "title": "A very nice title",
            "type": "video",
            "contentRef": "testmock:sampleContent",
            "active": true
        }
    ]
"""

assets_template = """
        [
            {
                "owner": "testmock",
                "name": "%s",
                "title": "016b9e5f-c184-48ea-a5e2-6e6bc2d62791",
                "tags": [],
                "type": "video",
                "contentRef": "testmock:%s",
                "active": true
            },
            {
                "owner": "testmock",
                "name": "%s",
                "title": "192e78ad-25d1-47f8-b539-19053a2b4a6f",
                "type": "application",
                "contentRef": "testmock:%s",
                "active": true
            },
            {
                "owner": "testmock",
                "name": "%s",
                "title": "3bf33965-41fe-4f94-8aa9-63b6b8a379da",
                "type": "video",
                "contentRef": "testmock:%s",
                "active": true
            },
            {
                "owner": "testmock",
                "name": "%s",
                "title": "44c6170a-2c03-42ce-bfa3-101fec955188",
                "type": "application",
                "contentRef": "testmock:%s",
                "active": true
            },
            {
                "alternativeIdentifiers": {
                    "tel": "0800100100",
                    "said": "something"
                },
                "owner": "testmock",
                "name": "%s",
                "title": "A picture of the moon",
                "tags": [
                    "todo",
                    "usage:boxart"
                ],
                "scores": {
                    "imdb.a3431": 0.9,
                    "fuse": 2
                },
                "type": "video",
                "fullMediaType": "video/mp4",
                "fileFormat": "mp4",
                "fileSize": 1024,
                "checksum": "12558d3269d25852bd26548dc2654ca2",
                "contentRef": "testmock:%s",
                "availabilityStartAt": "2025-01-01T12:00:00.000Z",
                "availabilityEndAt": "2025-04-01T12:00:00.000Z",
                "active": true,
                "ratings": {
                    "BBFC": "PG"
                },
                "audienceTypes": [
                    "family",
                    "children"
                ],
                "languages": [
                    "en",
                    "it"
                ],
                "mediaInfo": {
                    "codec": "other",
                    "duration": "PT1H30M",
                    "bitrate": 250,
                    "dimensions": "2D",
                    "screenFormat": "widescreen",
                    "definition": "HD",
                    "resolution": "1080p",
                    "frameRate": 29.97,
                    "aspectRatio": "16:9",
                    "height": 1920,
                    "width": 1080,
                    "subtitleLanguages": [
                      "en",
                      "it"
                    ],
                "dubbedLanguages": [
                      "en",
                      "it"
                ],
                "videoTracks": [
                      {
                        "title": "Video track title",
                        "description": "Video track description",
                        "schema": "embedded-english-subtitles",
                        "codec": "H.264",
                        "duration": "PT1H30M",
                        "bitrate": 250,
                        "resolution": "1080p",
                        "frameRate": 29.97,
                        "aspectRatio": "16:9",
                        "height": 1920,
                        "width": 1080
                      }
                    ],
                "audioTracks": [
                      {
                        "title": "Audio track title",
                        "description": "Audio track description",
                        "language": "it",
                        "schema": "audio-description",
                        "codec": "AAC",
                        "duration": "PT1H30M",
                        "bitrate": 250,
                        "sampleRate": 250,
                        "channels": 1
                      }
                    ]
                },
                "protection": {
                    "scheme": "playready",
                    "contentId": "12345"
                }
            }
        ]
    """

assets_with_errors = """
    [
        {
            "owner": "testmock",
            "name": "3bf33965-41fe-4f94-8aa9-63b6b8a379da",
            "title": "3bf33965-41fe-4f94-8aa9-63b6b8a379da",
            "type": "video",
            "contentRef": "testmock:sampleContent",
            "active": true
        },
        {
            "owner": "testmock",
            "name": "44c6170a-2c03-42ce-bfa3-101fec955188",
            "title": "44c6170a-2c03-42ce-bfa3-101fec955188",
            "type": "application",
            "contentRef": "testmock:sampleContent",
            "active": "error"
        },
        {
            "alternativeIdentifiers": {
                "tel": "0800100100",
                "said": "something"
            },
            "owner": "testmock",
            "title": "A picture of the moon",
            "tags": [
                "todo",
                "usage:boxart"
            ],
            "scores": {
                "imdb.a3431": 0.9,
                "fuse": 2
            },
            "type": "video",
            "fullMediaType": "video/mp4",
            "fileFormat": "mp4",
            "fileSize": 1024,
            "checksum": "12558d3269d25852bd26548dc2654ca2",
            "contentRef": "testmock:sampleContent",
            "availabilityStartAt": "2025-01-01T12:00:00.000Z",
            "availabilityEndAt": "2025-04-01T12:00:00.000Z",
            "active": true,
            "ratings": {
                "BBFC": "PG"
            },
            "audienceTypes": [
                "family",
                "children"
            ],
            "languages": [
                "en",
                "it"
            ],
            "mediaInfo": {
                "codec": "other",
                "duration": "PT1H30M",
                "bitrate": 250,
                "dimensions": "2D",
                "screenFormat": "widescreen",
                "definition": "HD",
                "resolution": "1080p",
                "frameRate": 29.97,
                "aspectRatio": "16:9",
                "height": 1920,
                "width": 1080,
                "subtitleLanguages": [
                  "en",
                  "it"
                ],
            "dubbedLanguages": [
                  "en",
                  "it"
            ],
            "videoTracks": [
                  {
                    "title": "Video track title",
                    "description": "Video track description",
                    "schema": "embedded-english-subtitles",
                    "codec": "H.264",
                    "duration": "PT1H30M",
                    "bitrate": 250,
                    "resolution": "1080p",
                    "frameRate": 29.97,
                    "aspectRatio": "16:9",
                    "height": "error",
                    "width": 1080
                  }
                ],
            "audioTracks": [
                  {
                    "title": "Audio track title",
                    "description": "Audio track description",
                    "language": "it",
                    "schema": "audio-description",
                    "codec": "AAC",
                    "duration": "PT1H30M",
                    "bitrate": 250,
                    "sampleRate": 250,
                    "channels": 1
                  }
                ]
            },
            "protection": {
                "scheme": "playready",
                "contentId": "12345"
            }
        }
    ]
"""
