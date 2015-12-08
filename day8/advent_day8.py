import re


class Santa(object):

    def countCode(self, strings):
        total = 0
        for string in strings:
            total += len(string)
        return total

    def countLiterals(self, strings):
        total = 0
        for string in strings:
            string = eval(string)
            total += len(string)
        return total

    def extraCode(self, strings):
        total = 0
        for string in strings:
            total += len(re.escape(string))+2
        return total


def main():
    file = open('input.txt')
    strings = []

    for line in file:
        line = line.rstrip()
        strings.append(line)

    print("Problem one: {}".format(
        Santa().countCode(strings) - Santa().countLiterals(strings)))
    print("Problem two: {}".format(
        Santa().extraCode(strings) - Santa().countCode(strings)))

if __name__ == "__main__":
    main()
