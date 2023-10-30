#!/usr/bin/env python3
""" Module that contains the test suite for utils.py """

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Test class for the utils.access_nested_map function """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test case for the access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test case for the access_nested_map function for an exception """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """ Test class for the utils.get_json function """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mocked_get):
        """ Test case to acertain that the get_json function
            returns the expected result """
        mocked_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mocked_get.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """ Test class for the utils.memoize decorator """

    def test_memoize(self):
        """ Test case to acertain that the memoize decorator
            memoizes a function's output correctly """
        class TestClass:
            """ Test class to test the memoize decorator """

            def a_method(self):
                """ Method that returns a number """
                return 42

            @memoize
            def a_property(self):
                """ Method that returns a number """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked_method:
            mocked_method.return_value = 42
            instance = TestClass()
            self.assertEqual(instance.a_property, mocked_method.return_value)
            self.assertEqual(instance.a_property, mocked_method.return_value)
            mocked_method.assert_called_once()
