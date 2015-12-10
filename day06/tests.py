import unittest
from advent_day6 import Santa, Grid


class TestCases(unittest.TestCase):
    test = Santa()

    def test_allLights(self):
        grid = Grid()

        self.test.setLights(grid, ["turn on 0,0 through 999,999"])
        self.assertEqual(1000000, self.test.countLights(grid))
        self.test.setLights(grid, ["turn off 499,499 through 500,500"])
        self.assertEqual(999996, self.test.countLights(grid))

    def test_toggleLights(self):
        grid = Grid()

        self.test.setLights(grid, ["toggle 0,0 through 999,0"])
        self.assertEqual(1000, self.test.countLights(grid))

    def test_brightness(self):
        grid = Grid()

        self.test.setBrightness(grid, ["turn on 0,0 through 0,0"])
        self.assertEqual(1, self.test.countLights(grid))

    def test_maxBrightness(self):
        grid = Grid()

        self.test.setBrightness(grid, ["toggle 0,0 through 999,999"])
        self.assertEqual(2000000, self.test.countLights(grid))

    def test_getPoints(self):
        r = self.test.getPoints("turn off 622,863 through 798,863")

        self.assertEqual([622, 863, 798, 863], [r.x1, r.y1, r.x2, r.y2])

if __name__ == "__main__":
    unittest.main()
