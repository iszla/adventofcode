import unittest
from advent_day10 import Santa


class TestCases(unittest.TestCase):
    test = Santa()

    def test_LookAndSay(self):
        self.assertEqual("312211", self.test.lookAndSay("1", 5))
