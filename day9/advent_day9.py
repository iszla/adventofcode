# Solution stolen from:
# https://www.reddit.com/r/adventofcode/comments/3w192e/day_9_solutions/cxsix3u
import sys
from itertools import permutations


class Santa(object):

    def parseInput(self, listInput, places, distances):
        for line in listInput:
            (source, _, dest, _, distance) = line.split()
            places.add(source)
            places.add(dest)
            distances.setdefault(source, dict())[dest] = int(distance)
            distances.setdefault(dest, dict())[source] = int(distance)

    def findRoutes(self, places, dists):
        shortest = sys.maxsize
        longest = 0
        for items in permutations(places):
            dist = sum(map(lambda x, y: dists[x][y], items[:-1], items[1:]))
            shortest = min(shortest, dist)
            longest = max(longest, dist)
        return {"shortest": shortest, "longest": longest}


def main():
    func = Santa()
    f = open("input.txt")
    inputList = []
    for l in f:
        inputList.append(l)

    places = set()
    distances = dict()

    func.parseInput(inputList, places, distances)
    dist = func.findRoutes(places, distances)
    print("Shortest route is {} units long".format(dist["shortest"]))
    print("Longest route is {} units long".format(dist["longest"]))

if __name__ == "__main__":
    main()
