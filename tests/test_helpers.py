import unittest


def helper_function(x):
    return x * 2


class TestHelpers(unittest.TestCase):
    def test_helper_function(self):
        self.assertEqual(helper_function(2), 4)
        self.assertEqual(helper_function(0), 0)
        self.assertEqual(helper_function(-1), -2)
