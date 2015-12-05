import unittest
from advent_day5_tdd import Santa


class TestCases(unittest.TestCase):

    def test_NaughtyOrNice(self):
        test = Santa()

        self.assertTrue(test.isNice("ugknbfddgicrmopn"))
        self.assertTrue(test.isNice("aaa"))
        self.assertFalse(test.isNice("jchzalrnumimnmhp"))
        self.assertFalse(test.isNice("haegwjzuvuyypxyu"))
        self.assertFalse(test.isNice("dvszwmarrgswjxmb"))

    def test_Naughtier(self):
        test = Santa()

        self.assertTrue(test.isNicer("qjhvhtzxzqqjkmpb"))
        self.assertTrue(test.isNicer("xxyxx"))
        self.assertFalse(test.isNicer("uurcxstgmygtbstg"))
        self.assertFalse(test.isNicer("ieodomkazucvgmuy"))

if __name__ == "__main__":
    unittest.main()
