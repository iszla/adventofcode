import unittest
from advent_day9 import Santa


class TestCases(unittest.TestCase):
    test = Santa()
    f = open("test_input.txt")
    ilist = []
    places = set()
    distances = dict()
    for line in f:
        ilist.append(line)

    def test_Distance(self):
        self.test.parseInput(self.ilist, self.places, self.distances)

        self.assertEqual(605, self.test.findRoutes(
            self.places, self.distances)["shortest"])

        self.assertEqual(982, self.test.findRoutes(
            self.places, self.distances)["longest"])
