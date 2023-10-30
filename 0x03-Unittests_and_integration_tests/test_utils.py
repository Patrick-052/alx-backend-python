#!/usr/bin/env python3
""" Module that contains the test suite for utils.py """

from unittest import TestCase
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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
