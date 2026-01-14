import unittest


class TestIntegration(unittest.TestCase):
    def test_multiple_operations(self):
        result = 0
        for i in range(5):
            result += i
        self.assertEqual(result, 10)
    
    def test_string_operations(self):
        text = "hello world"
        self.assertEqual(text.upper(), "HELLO WORLD")
        self.assertEqual(text.split(), ["hello", "world"])
