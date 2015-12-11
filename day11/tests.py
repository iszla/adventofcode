import unittest
from advent_day11 import Santa


class TestCases(unittest.TestCase):
    test = Santa()

    def test_ValidationFalse(self):
        self.assertFalse(self.test.validate("hijklmmn"))
        self.assertFalse(self.test.validate("abbceffg"))
        self.assertFalse(self.test.validate("abbcegjk"))

    def test_ValidationTrue(self):
        self.assertTrue(self.test.validate("abckmmnn"))
        self.assertTrue(self.test.validate("abbcdffg"))
        self.assertTrue(self.test.validate("aabceggk"))

    def test_generation(self):
        self.assertEqual("cqjxxyzz", self.test.generate("cqjxjnds"))
        self.assertEqual("cqkaabcc", self.test.generate("cqjxxyzz"))
        self.assertEqual("abcdffaa", self.test.generate("abcdefgh"))

    def test_generationLong(self):
        self.assertEqual("ghjaabcc", self.test.generate("ghijklmn"))
