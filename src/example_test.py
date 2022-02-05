import unittest
import example

class TestExample(unittest.TestCase):

    def test_quick(self):
        self.assertEqual(example.quick(), 1)

    def test_slow(self):
        self.assertEqual(example.slow(), 10)

    def test_flakey(self):
        self.assertEqual(example.flakey(), 1)
