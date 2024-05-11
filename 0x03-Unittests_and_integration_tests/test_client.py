#!/usr/bin/env python3"
""" Testing functions of the client module """


from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch, PropertyMock


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

    def test_public_repos_url(self):
        """ Function that tests: GithubOrgClient._public_repos_url function"""
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)\
             as mock_org:
            mock_org.return_value = {"repos_url": {"payload": True}}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, {"payload": True})

    @patch("client.get_json",
           return_value=[{"name": "repo1"}, {"name": "repo2"}])
    def test_public_repos(self, mock_get_json) -> None:
        """doc doc doc"""
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            github_org_client = GithubOrgClient("google")
            self.assertEqual(github_org_client.public_repos(),
                             ["repo1", "repo2"])
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
