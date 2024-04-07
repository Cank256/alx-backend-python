#!/usr/bin/env python3

"""
This module contains unit tests for the utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from functools import wraps

class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """
        Test that access_nested_map raises a KeyError when expected.
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), "Key not found")

class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Test the get_json function.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        result = get_json(test_url)
        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """
    Test case for the memoize decorator.
    """

    class TestClass:
        """
        Test class with memoized method.
        """

        def a_method(self):
            """
            Test method.
            """
            return 42

        @memoize
        def a_property(self):
            """
            Test method with memoization.
            """
            return self.a_method()

    def test_memoize(self):
        """
        Test memoization functionality.
        """
        test_instance = self.TestClass()

        with patch.object(test_instance, "a_method", return_value=42) as mock_a_method:
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

if __name__ == "__main__":
    unittest.main()
