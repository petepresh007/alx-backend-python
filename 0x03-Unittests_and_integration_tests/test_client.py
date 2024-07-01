#!/usr/bin/env python3
'''a module for client test'''
import unittest
from unittest.mock import patch
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


if __name__ == "__main__":
    unittest.main()
