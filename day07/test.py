import unittest
from advent_day7 import Santa


class TestCases(unittest.TestCase):
    test = Santa()

    def test_TestOne(self):
        steps = ["123 -> x", "456 -> y", "x AND y -> d", "x OR y -> e",
                 "x LSHIFT 2 -> f", "y RSHIFT 2 -> g", "NOT x -> h",
                 "NOT y -> i"]

        c = {}

        self.test.build(c, steps)

        print("....")

        self.assertEqual(72, c["d"])
        self.assertEqual(507, c["e"])
        self.assertEqual(492, c["f"])
        self.assertEqual(114, c["g"])
        self.assertEqual(65412, c["h"])
        self.assertEqual(65079, c["i"])
        self.assertEqual(123, c["x"])
        self.assertEqual(456, c["y"])
