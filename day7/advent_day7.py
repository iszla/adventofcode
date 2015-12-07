import struct


class Santa(object):

    def build(self, circuit, steps):
        index = 0
        for step in steps:
            steps[index] = self.parse(step)
            index += 1

        bigindex = 0
        while len(steps) > 0:
            bigindex += 1
            if bigindex > 600:
                print("Instrucation set broken")
                break
            index = 0
            for step in steps:
                try:
                    exec(step)
                    passed = True
                except KeyError:
                    passed = False
                if passed:
                    steps.pop(index)
                index += 1
            self.allTo16Bit(circuit)

    def intTo16Bit(self, num):
        return struct.unpack('H', struct.pack('h', num))[0]

    def allTo16Bit(self, circuit):
        for key, value in circuit.items():
            if value < 0:
                circuit[key] = struct.unpack('H', struct.pack('h', value))[0]

    def parse(self, step):
        c = "circuit"
        newStep = ""
        input = True
        parts = step.split(" ")
        for part in parts:
            part = part.rstrip()
            if input:
                if part == "AND":
                    newStep += " & "
                elif part == "OR":
                    newStep += " | "
                elif part == "LSHIFT":
                    newStep += " << "
                elif part == "RSHIFT":
                    newStep += " >> "
                elif part == "NOT":
                    newStep += " ~ "
                elif part == "->":
                    input = False
                elif part.isnumeric():
                    newStep += str(self.intTo16Bit(int(part)))
                else:
                    newStep += c+"[\""+part+"\"]"
            else:
                newStep = c+"[\""+part+"\"] = " + newStep

        return newStep


def main():
    mech = Santa()
    circuit = {}

    steps = open("input.txt")
    allSteps = []
    for step in steps:
        allSteps.append(step)

    mech.build(circuit, allSteps)
    print("The value of a is: {0}".format(circuit["a"]))

if __name__ == "__main__":
    main()
