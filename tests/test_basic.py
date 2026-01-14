import unittest


class TestBasic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    
    def test_string(self):
        self.assertEqual("hello", "hello")
    
    def test_list(self):
        test_list = [1, 2, 3]
        self.assertEqual(len(test_list), 3)


if __name__ == '__main__':
    unittest.main()
