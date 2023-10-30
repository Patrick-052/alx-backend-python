#!/usr/bin/env python3
""" Module that contains the test suite for client.py """

from unittest import TestCase
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
