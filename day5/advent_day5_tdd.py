import unittest


class Santa(object):

    def isNice(self, name):
        vowels = 0
        double = False

        if any(combo in name for combo in ["ab", "cd", "pq", "xy"]):
            return False

        for x in range(0, len(name)):
            if name[x] in "aeiou":
                vowels += 1

            if x < len(name) - 1:
                if name[x] == name[x+1]:
                    double = True

        if double and vowels > 2:
            return True

        return False

    def isNicer(self, name):
        pairs = 0
        skip = 0

        for x in range(0, len(name)):
            if x < len(name) - 2:
                if name[x] == name[x+2]:
                    skip += 1
                # Add space in the string I am comparing agains
                # otherwise it will lead to false positives
                # example: mmggfwapsetemiuj
                if name[x]+name[x+1] in name[:x]+" "+name[x+2:]:
                    pairs += 1

        if pairs > 0 and skip > 0:
            return True

        return False


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


def main():
    check = Santa()
    nice = 0
    nicer = 0

    theList = open("list.txt")

    for line in theList:
        if check.isNice(line):
            nice += 1

        if check.isNicer(line):
            nicer += 1

    print("There are {0} nice strings".format(nice))
    print("There are {0} nicer strings".format(nicer))

if __name__ == "__main__":
    # unittest.main()
    main()
