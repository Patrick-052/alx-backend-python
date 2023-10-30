#!/usr/bin/env python3
""" Module that contains the test suite for client.py """

from unittest import TestCase
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import unittest
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """ Test class for the GithubOrgClient class """

    @parameterized.expand([
        'google',
        'abc'
        ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mocked_get):
        """ Test case to acertain that the GithubOrgClient.org
            method returns the correct value """
        test_org_url = f'https://api.github.com/orgs/{test_org_name}'
        mocked_get.return_value = {"payload": True}
        github_client = GithubOrgClient(test_org_name)
        self.assertEqual(github_client.org, mocked_get.return_value)

    def test_public_repos_url(self):
        """ Test case to acertain that the _public_repos_url
            method returns the correct value """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mocked_org:
            mocked_org.return_value = {"repos_url": "test_url"}
            github_client = GithubOrgClient('test')
            self.assertEqual(github_client._public_repos_url, "test_url")

    @patch('client.get_json')
    def test_public_repos(self, mocked_get):
        """ Test case to acertain that the public_repos method
            returns the correct value """
        mocked_get.return_value = [{"name": "google"},
                                   {"name": "abc"}]
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mocked_public:
            mocked_public.return_value = "test_url"
            github_client = GithubOrgClient('test')
            self.assertEqual(github_client.public_repos(),
                             ["google", "abc"])
            mocked_get.assert_called_once_with("test_url")

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
        ])
    def test_has_license(self, repo, license_key, expected):
        """ Test case to acertain that the has_license method
            returns the correct value """
        github_client = GithubOrgClient('test')
        self.assertEqual(github_client.has_license(repo, license_key), expected)


def requests_get(*args, **kwargs):
    """
    Function that mocks requests.get function
    Returns the correct json data based on the given input url
    """
    class MockResponse:
        """
        Mock response
        """

        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == "https://api.github.com/orgs/google":
        return MockResponse(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for the GithubOrgClient.public_repos method
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up function for TestIntegrationGithubOrgClient class
        Sets up a patcher to be used in the class methods
        """
        cls.get_patcher = patch('utils.requests.get', side_effect=requests_get)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """
        Tear down resources set up for class tests.
        Stops the patcher that had been started
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method without license
        """
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with license
        """
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos)
