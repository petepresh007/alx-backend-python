#!/usr/bin/env python3
'''a module to create a test case'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''a class for the test case'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test that a KeyError is raised for the respective inputs """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    '''get json class'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        '''creating a mock get'''
        with patch('utils.requests.get') as mocked_get:
            # Create a mock response object with a json method that returns
            mocked_response = Mock()
            mocked_response.json.return_value = test_payload
            mocked_get.return_value = mocked_response

            # Call the function with the test URL
            result = get_json(test_url)

            # Assert the mocked get method was called exactly once with test_ur
            mocked_get.assert_called_once_with(test_url)

            # Assert that the function's output is equal to test_payload
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                'a_method',
                return_value=42
                ) as mocked_method:
            test_instance = TestClass()
            # Call a_property twice
            result_first_call = test_instance.a_property
            result_second_call = test_instance.a_property

            # Assert the mocked a_method was called exactly once
            mocked_method.assert_called_once()

            # Assert the results of both calls are the same and correct
            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)


if __name__ == "__main__":
    unittest.main()
