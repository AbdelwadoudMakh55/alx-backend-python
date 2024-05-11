#!/usr/bin/env python3"
"""
Testing functions of the client module
"""


from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for testing "client.GithubOrgClient.org"
    """

    @parameterized.expand([
        ("google", {"name": None}),
        ("abc", {"name": None})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, response: Dict,
                 mock_get_json: unittest.mock.MagicMock) -> None:
        """ Function that test: GithubOrgClient.org function"""
        org_client = GithubOrgClient(org)
        url = GithubOrgClient.ORG_URL.format(org=org)
        mock_get_json.return_value = response
        self.assertEqual(org_client.org, response)
        mock_get_json.assert_called_once_with(url)
