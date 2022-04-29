with open("input.txt") as f:
    rawinput = [line.replace("\n", "") for line in f.readlines()]


def partone():
    """Identify corrupted chunks and calculate error score"""
    brackets = {"(": ")",
                "[": "]",
                "{": "}",
                "<": ">"}
    corruptedlist = []
    incompletelist = []
    errorscore = []

    for ei, entry in enumerate(rawinput):
        corrupted = False
        entrycopy = []
        for xi, x in enumerate(entry):
            if x in brackets.keys(): # open bracket
                entrycopy.append(x)
            elif x in brackets.values(): # close bracket
                if brackets.get(entrycopy[-1]) == x:
                    entrycopy.pop()
                else:
                    corrupted = True
                    corruptedlist.append((ei, brackets.get(entrycopy[-1]), x)) # index, expected, actual
                    break
        if corrupted is False:
            incompletelist.append("".join(entrycopy))

    for entry in corruptedlist:
        if entry[2] == ")":
            errorscore.append(3)
        elif entry[2] == "]":
            errorscore.append(57)
        elif entry[2] == "}":
            errorscore.append(1197)
        elif entry[2] == ">":
            errorscore.append(25137)

    print(f"Syntax error score: {sum(errorscore)}")

    return brackets, incompletelist


def parttwo(brackets, incompletelist):
    """Complete incomplete chunks and calculate completion score"""
    completed = []
    completionscores = []

    for entry in incompletelist:
        entrycopy = []
        for x in entry:
            entrycopy.insert(0, brackets.get(x))
        completed.append("".join(entrycopy))

    for complete in completed:
        score = 0
        for bracket in complete:
            score = score * 5
            if bracket == ")":
                score += 1
            elif bracket == "]":
                score += 2
            elif bracket == "}":
                score += 3
            elif bracket == ">":
                score += 4
        completionscores.append(score)

    completionscores.sort()
    middleindex = int((len(completionscores) - 1) / 2)
    print(f"Middle completion score: {completionscores[middleindex]}")


def main():
    brackets, incompletelist = partone()
    parttwo(brackets, incompletelist)


if __name__ == "__main__":
    main()
