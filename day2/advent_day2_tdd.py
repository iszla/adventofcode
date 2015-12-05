import unittest


class Santa(object):

    def wrapping(self, presents):
        totalPaper = 0

        for present in presents:
            present = list(map(int, present.split("x")))
            first = present[0]
            present[0] = 2 * (present[0]*present[1])
            present[1] = 2 * (present[1]*present[2])
            present[2] = 2 * (present[2]*first)
            small = min(present) / 2

            totalPaper += present[0] + present[1] + present[2] + small

        return totalPaper

    def ribbon(self, presents):
        totalRibbon = 0

        for present in presents:
            present = list(map(int, present.split("x")))
            present = sorted(present)
            wrap = present[0] + present[0] + present[1] + present[1]
            bow = present[0] * present[1] * present[2]
            totalRibbon += wrap + bow

        return totalRibbon


class TestCases(unittest.TestCase):

    def test_ProblemOne(self):
        test = Santa()

        self.assertEqual(58, test.wrapping(["2x3x4"]))
        self.assertEqual(43, test.wrapping(["1x1x10"]))

    def test_ProblemTwo(self):
        test = Santa()

        self.assertEqual(34, test.ribbon(["2x3x4"]))
        self.assertEqual(14, test.ribbon(["1x1x10"]))


def main():
    presents = []
    santa = Santa()

    file = open("presents.txt")

    for present in file:
        presents.append(present)

    print("Total paper needed: {0}".format(santa.wrapping(presents)))
    print("Total ribbon needed: {0}".format(santa.ribbon(presents)))

if __name__ == "__main__":
    # unittest.main()
    main()
