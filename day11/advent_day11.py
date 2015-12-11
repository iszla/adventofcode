class Santa(object):
    alpha = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", \
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    fullAlpha = "abcdefghijklmnopqrstuvwxyz"
    num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7,
           "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
           "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21,
           "w": 22, "x": 23, "y": 24, "z": 25}

    def generate(self, string):
        cString = list(string[::-1])
        while True:
            for x in range(len(string)):
                rotate = True
                char = cString[x]
                if char == "z":
                    rotate = False
                char = self.getNextChar(char)
                cString[x] = char
                if rotate:
                    break
            cString = ''.join(cString[::-1])
            if self.validate(cString):
                return cString
            cString = list(cString[::-1])

    def getNextChar(self, char):
        char = str(char)
        number = self.num[char]
        if number == 25:
            return self.alpha[0]

        return self.alpha[number+1]

    def validate(self, string):
        doubles = set()
        rise = False

        if any(l in string for l in ["i", "o", "l"]):
            return False

        for x in range(len(string)):
            if x < len(string) - 2:
                if string[x:x+3] in self.fullAlpha:
                    rise = True

            if x < len(string) - 1:
                if string[x] == string[x+1]:
                    doubles.add(x)
                    doubles.add(x+1)

        if rise and len(doubles) > 3:
            return True

        return False


def main():
    newPass = Santa().generate("cqjxjnds")
    print(newPass)
    print(Santa().generate(newPass))

if __name__ == "__main__":
    main()
