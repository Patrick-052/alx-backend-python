#!/usr/bin/env python3
""" Module that contains the test suite for utils.py """

from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ Test class for the utils functions """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test case for the access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)
