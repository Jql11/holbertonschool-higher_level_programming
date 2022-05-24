#!/usr/bin/python3
"""Unitest - Module to find the max integer in a list
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_signed_ints_floats(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, 1, 2]), 2)
        self.assertEqual(max_integer([-1.5, 3.2, -5]), 3.2)
        self.assertEqual(max_integer([{1, 3}, {4, 2}]), {1, 3})

    def test_infinity(self):
        self.assertEqual(max_integer([1, 2, float('inf')]), float('inf'))

    def test_no_argument(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

    def test_list_string(self):
        self.assertEqual(max_integer(["hello", "world"]), 'world')
        self.assertEqual(max_integer("abcxyz"), 'z')
        self.assertEqual(max_integer(['a', 'b', 'c', 'x', 'y', 'z']), 'z')

    def test_list(self):
        self.assertEqual(max_integer([[1, 3], [4, 2]]), [4, 2])

    def test_failed(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3})
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 3])
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3}, {1, 2})
        with self.assertRaises(TypeError):
            max_integer([1, 2], [3, 4])
        with self.assertRaises(TypeError):
            max_integer([None, False])


if __name__ == "__main__":
    unittest.main()
