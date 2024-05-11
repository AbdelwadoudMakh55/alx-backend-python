#!/usr/bin/env python3"
"""
Testing functions of the client module
"""


from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for testing "client.GithubOrgClient.org"
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """ Function that test: GithubOrgClient.org function"""
        org_client = GithubOrgClient(org)
        url = GithubOrgClient.ORG_URL.format(org=org)
        mock_get_json.return_value = {"name": None}
        self.assertEqual(org_client.org, {"name": None})
        mock_get_json.assert_called_once_with(url)
