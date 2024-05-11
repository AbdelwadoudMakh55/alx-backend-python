#!/usr/bin/env python3
"""
Module for parameterized testing
"""


import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for testing "client.GithubOrgClient.org"
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, client, mock_get_json):
        """ Function that test: GithubOrgClient.org function"""
        mock_response = {"name": None}
        org_client = GithubOrgClient(client)
        url = GithubOrgClient.ORG_URL.format(org=client)
        mock_get_json.return_value = mock_response
        self.assertEqual(org_client.org, mock_response)
        mock_get_json.assert_called_once_with(url)
