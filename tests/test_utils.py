import unittest


class TestUtils(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual([], [])
    
    def test_dict_access(self):
        test_dict = {"key": "value"}
        self.assertEqual(test_dict["key"], "value")
    
    def test_boolean(self):
        self.assertTrue(True)
        self.assertFalse(False)
