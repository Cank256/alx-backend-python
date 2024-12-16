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
    """Test cases for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the correct value.

        Args:
            nested_map: The dictionary to traverse.
            path: The keys to traverse through the dictionary.
            expected: The expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
        self, nested_map, path, expected_error_key
    ):
        """
        Test that access_nested_map raises KeyError when key is not found.

        Args:
            nested_map: The dictionary to traverse.
            path: The keys to traverse through the dictionary.
            expected_error_key: The missing key expected to raise the error.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_error_key}'")


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
    Unit tests for the `memoize` decorator.

    The `memoize` decorator is used to cache the result of a method call.
    When the decorated method is accessed multiple times, the cached result
    is returned instead of recalculating the result.
    """

    def test_memoize(self):
        """
        Test that the `memoize` decorator caches the result of a method call.

        The test verifies the following:
        - The decorated method is executed only once, even when accessed
        multiple times.
        - The cached value is returned on subsequent accesses, without
        calling the original method again.

        A mock object is used to track calls to the original method.
        """
        class TestClass:
            """
            A test class to demonstrate the `memoize` decorator.

            Attributes:
                a_method: A regular method that returns a fixed value.
                a_property: A property decorated with `memoize` that calls
                            `a_method`.
            """

            def a_method(self):
                """
                A simple method to return a fixed value.

                Returns:
                    int: The fixed value 42.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A memoized property that calls `a_method` and caches the result

                Returns:
                    int: The result of calling `a_method`, cached after the
                    first call.
                """
                return self.a_method()

        # Use a mock to track calls to the `a_method`.
        with patch.object(TestClass, 'a_method', return_value=42)
        as mock_method:
            obj = TestClass()

            # Assert that the first access to `a_property` calls `a_method`.
            self.assertEqual(obj.a_property, 42)

            # Assert that subsequent accesses do not call `a_method` again.
            self.assertEqual(obj.a_property, 42)

            # Verify that `a_method` was only called once due to memoization.
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
