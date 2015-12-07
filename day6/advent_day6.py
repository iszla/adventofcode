import re


class Ponits(object):

    def __init__(self):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None


class Grid(list):

    def __init__(self):
        for x in range(1000):
            self.append([])
            for y in range(1000):
                self[x].append(0)


class Santa(object):

    def countLights(self, grid):
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] > 0:
                    count += grid[x][y]
        return count

    def setLights(self, grid, instructions):
        for line in instructions:
            points = self.getPoints(line)
            if line.startswith("turn on"):
                for x in range(points.x1, points.x2+1):
                    for y in range(points.y1, points.y2+1):
                        grid[x][y] = 1
            if line.startswith("turn off"):
                for x in range(points.x1, points.x2+1):
                    for y in range(points.y1, points.y2+1):
                        grid[x][y] = 0
            if line.startswith("toggle"):
                for x in range(points.x1, points.x2+1):
                    for y in range(points.y1, points.y2+1):
                        if grid[x][y] == 1:
                            grid[x][y] = 0
                        else:
                            grid[x][y] = 1

    def setBrightness(self, grid, instructions):
        for line in instructions:
            points = self.getPoints(line)
            if line.startswith("turn on"):
                for x in range(points.x1, points.x2+1):
                    for y in range(points.y1, points.y2+1):
                        grid[x][y] += 1
            if line.startswith("turn off"):
                for x in range(points.x1, points.x2+1):
                    for y in range(points.y1, points.y2+1):
                        if grid[x][y] > 0:
                            grid[x][y] -= 1
            if line.startswith("toggle"):
                for x in range(points.x1, points.x2+1):
                    for y in range(points.y1, points.y2+1):
                        grid[x][y] += 2

    def getPoints(self, line):
        m = re.match(".* (\d+,\d+).* (\d+,\d+)", line)
        r = Ponits()
        r.x1, r.y1 = m.group(1).split(",")
        r.x2, r.y2 = m.group(2).split(",")
        r.x1, r.y1, r.x2, r.y2 = int(r.x1), int(r.y1), int(r.x2), int(r.y2)
        return r


def main():
    santa = Santa()
    f = open("input.txt")
    instructions = []
    for line in f:
        instructions.append(line)

    grid = Grid()
    santa.setLights(grid, instructions)
    count = santa.countLights(grid)

    print("There are {0} lights turned on.".format(count))

    grid = Grid()
    santa.setBrightness(grid, instructions)
    count = santa.countLights(grid)

    print("The total brightness is {0}".format(count))


if __name__ == "__main__":
    main()
