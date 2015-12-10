import unittest
from advent_day8 import Santa


class TestCases(unittest.TestCase):
    test = Santa()
    file = open('test.txt')
    strings = []

    for line in file:
        line = line.rstrip()
        strings.append(line)

    def test_code(self):

        summa = self.test.countCode(self.strings)
        self.assertEqual(69, summa)

    def test_literals(self):

        summa = self.test.countLiterals(self.strings)
        self.assertEqual(38, summa)

    def test_problemOne(self):

        sumCode = self.test.countCode(self.strings)
        sumLit = self.test.countLiterals(self.strings)
        self.assertEqual(31, sumCode - sumLit)

    def test_problemTwo(self):

        sumExtra = self.test.extraCode(self.strings)
        sumCode = self.test.countCode(self.strings)
        self.assertEqual(37, sumExtra - sumCode)
