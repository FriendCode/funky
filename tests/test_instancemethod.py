# Imports
import random
import unittest
from funky import memoize, timed_memoize


class Dummy(object):
    @memoize
    def a(self):
        return random.random()


class TestInstanceMethod(unittest.TestCase):
    def test_dummy(self):
        dummy = Dummy()
        v1 = dummy.a()
        v2 = dummy.a()
        dummy.a.clear()
        v3 = dummy.a()
        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)


if __name__ == '__main__':
    unittest.main()
