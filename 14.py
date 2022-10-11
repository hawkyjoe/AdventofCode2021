# --- Day 14: Extended Polyermization ---
from collections import Counter


def inp():
    """Input processing"""
    instructions = []
    with open("input.txt") as f:
        template = f.readline().replace("\n", "")
        for line in f.readlines():
            if line != "\n":
                instructions.append(tuple(line.replace("\n", "").split(" -> ")))
    print(template, instructions)
    return template, instructions


def partone(template, instructions):
    """Pair insertion with positions"""
    templatelist = list(template)
    pairs = (list(zip(*instructions))[0]) # extract pairs

    for n in range(10):
        toinsert = []
        for i, x in enumerate(templatelist):
            if i == 0: # first index has no i-1
                continue
            for pi, pair in enumerate(pairs):
                if templatelist[i-1] + x == pair:
                    toinsert.append((i, instructions[pi][1]))
        for i, x in (reversed(toinsert)): #reversed to avoid index frameshifting
            templatelist.insert(i, x)

    result = Counter(templatelist).most_common()[0][1] - Counter(templatelist).most_common()[-1][1]
    print(f"The difference between the most and least common elements is {result}")


def parttwo(template, instructions):

    """Pair insertion without positions"""
    # store as counters

    inserts = list(zip(*instructions))[1]
    pairs = list(zip(*instructions))[0]

    # counting template
    templatepairs = []
    for x in range(len(template)-1):
        templatepairs.append(template[x:x+2])
    paircounter = Counter(templatepairs)
    elementcounter = Counter(template)

    print(paircounter)

    for x in range(10):
        add = [] # new pairs to add to count
        remove = [] # old pairs to remove from count
        for pair, freq in paircounter.items():
            if pair in pairs:
                insert = inserts[pairs.index(pair)]
                add.extend(freq * [pair[0] + insert, insert + pair[1]])
                remove.extend(freq * [pair])
                elementcounter.update(freq * insert)

        paircounter.update(add) # outside loop to avoid dictionary size change during iteration error

        for pair in remove:
            paircounter[pair] = paircounter[pair] - 1
            if paircounter[pair] == 0:
                del paircounter[pair]

    print(elementcounter, paircounter)

    print(elementcounter.most_common()[0][1] - elementcounter.most_common()[-1][1])


def main():
    template, instructions = inp()
    # partone(template, instructions)
    parttwo(template, instructions)


main()
