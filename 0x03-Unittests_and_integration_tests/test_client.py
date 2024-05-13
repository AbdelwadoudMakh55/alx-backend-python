#!/usr/bin/env python3
"""
Unittesting of "client.py" using patchers and parameterized
"""


import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Testing the GithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", return_value={"name": None})
    def test_org(self, org, mock_get_json):
        """ Test test_org """
        client = GithubOrgClient(org)
        url = GithubOrgClient.ORG_URL.format(org=org)
        self.assertEqual(client.org, {"name": None})
        mock_get_json.assert_called_once_with(url)
