# Imports
import random
import unittest
from funky import memoize


class Dummy(object):
    @memoize
    def a(self):
        return random.random()


class TestInstanceMethod(unittest.TestCase):
    def test_dummy(self):
        dummy = Dummy()
        dummy2 = Dummy()

        v1 = dummy.a()
        x1 = dummy2.a()
        v2 = dummy.a()
        x2 = dummy2.a()
        dummy.a.clear()
        v3 = dummy.a()
        x3 = dummy2.a()

        self.assertEqual(v1, v2)
        self.assertEqual(x1, x2)
        self.assertNotEqual(v1, x1)

        self.assertNotEqual(v1, v3)
        self.assertNotEqual(v3, x3)


if __name__ == '__main__':
    unittest.main()
