#!/usr/bin/env python3

"""
This module contains unit tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized_class(("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
                         [(None, None, None, None)],
                         indirect=True)
    class IntegrationGithubOrgClient(unittest.TestCase):
        """
        Integration test case for the GithubOrgClient class.
        """

        @classmethod
        def setUpClass(cls, org_payload, repos_payload, expected_repos, apache2_repos):
            """
            Set up fixtures for the integration tests.
            """
            cls.org_payload = org_payload
            cls.repos_payload = repos_payload
            cls.expected_repos = expected_repos
            cls.apache2_repos = apache2_repos

            cls.get_patcher = patch("client.requests.get")
            cls.mock_get = cls.get_patcher.start()

            cls.mock_get.side_effect = [
                Mock(json=lambda: cls.org_payload),
                Mock(json=lambda: cls.repos_payload)
            ]

        @classmethod
        def tearDownClass(cls):
            """
            Tear down the patcher.
            """
            cls.get_patcher.stop()

        def test_public_repos(self):
            """
            Test public_repos method.
            """
            client = GithubOrgClient("google")
            repos = client.public_repos()
            self.assertEqual(repos, self.expected_repos)

        def test_public_repos_with_license(self):
            """
            Test public_repos method with license argument.
            """
            client = GithubOrgClient("google")
            repos = client.public_repos("apache-2.0")
            self.assertEqual(repos, self.apache2_repos)

if __name__ == "__main__":
    unittest.main()
