import unittest


class Santa(object):

    def move(self, route):
        floor = 0

        for x in range(0, len(route)):
            floor += +1 if route[x] == "(" else -1

        return floor

    def basement(self, route):
        floor = 0
        first = -1

        for x in range(0, len(route)):
            floor += +1 if route[x] == "(" else -1
            if floor < 0 and first < 0:
                return x + 1

        return floor


class TestCases(unittest.TestCase):

    def test_ProblemOne(self):
        tests = Santa()

        self.assertEqual(0, tests.move("(())"))
        self.assertEqual(0, tests.move("()()"))
        self.assertEqual(3, tests.move("((("))
        self.assertEqual(3, tests.move("(()(()("))
        self.assertEqual(-1, tests.move("())"))
        self.assertEqual(-3, tests.move(")())())"))

    def test_ProblemTwo(self):
        tests = Santa()

        self.assertEqual(1, tests.basement(")"))
        self.assertEqual(5, tests.basement("()())"))


def main():
    file = open("route.txt", 'r')
    route = file.read()
    santa = Santa()

    print("Santa ends up on floor {0}".format(santa.move(route)))
    print("He first enters the basement on step {0}".format(
        santa.basement(route)))

if __name__ == "__main__":
    # unittest.main()
    main()
