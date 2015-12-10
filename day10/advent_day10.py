class Santa(object):

    def lookAndSay(self, inputString, iterations):

        for x in range(iterations):
            output = ""
            repeats = 1
            for y in range(len(inputString)):
                if y < len(inputString) - 1:
                    if inputString[y] == inputString[y+1]:
                        repeats += 1
                    else:
                        output += str(repeats) + inputString[y]
                        repeats = 1
                else:
                    output += str(repeats) + inputString[y]
                    repeats = 1
            inputString = output
        return output


def main():
    output = Santa().lookAndSay("1113222113", 40)
    output2 = Santa().lookAndSay(output, 10)

    print("First: {} Second: {}".format(len(output), len(output2)))

if __name__ == "__main__":
    main()
