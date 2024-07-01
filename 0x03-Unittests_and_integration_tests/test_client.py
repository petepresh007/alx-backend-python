#!/usr/bin/env python3
'''a module for client test'''
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    '''a class to text git hub'''
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"login": "sample_org"})
    def test_org(self, org_name, mock_get_json):
        '''Instantiate the GithubOrgClient with the org_name'''
        client = GithubOrgClient(org_name)

        # Call the org property
        result = client.org

        # Assert that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )

        # Assert that the result is correct
        self.assertEqual(result, {"login": "sample_org"})


class TestGithubOrgClient(unittest.TestCase):
    '''a class to mock'''
    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    def test_public_repos_url(self, org_name, expected_url):
        '''methods with parameters'''
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock
                ) as mock_org:
            # Mock the org property to return a payload with the expected URL
            mock_org.return_value = {"repos_url": expected_url}

            # Instantiate the GithubOrgClient with the org_name
            client = GithubOrgClient(org_name)

            # Assert that _public_repos_url returns the expected URL
            self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
