import unittest

from bin.parser import Parser

class TestParser(unittest.TestCase):
    def test_type_url(self):
        self.assertRaises(TypeError,Parser,3)


if __name__ == '__main__':
    unittest.main()
