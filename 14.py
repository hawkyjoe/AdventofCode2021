# --- Day 14: Extended Polyermization ---
from collections import Counter
import time
start = time.time()


def inp():
    """Input processing"""
    instructions = []
    with open("input_14.txt") as f:
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
    print(Counter(templatelist))
    print(f"The difference between the most and least common elements is {result}")


def parttwo(template, instructions):
    """Pair insertion without positions"""
    inserts = list(zip(*instructions))[1]
    pairs = list(zip(*instructions))[0]

    # counting template
    templatepairs = []
    for x in range(len(template)-1):
        templatepairs.append(template[x:x+2])
    paircounter = Counter(templatepairs)
    elementcounter = Counter(template)

    for x in range(10):
        add = {} # new pairs to add to count
        remove = {} # old pairs to remove from count
        for pair, freq in paircounter.items():
            if pair in pairs and freq > 0:
                insert = inserts[pairs.index(pair)]
                add[pair[0] + insert] = add.get(pair[0] + insert, 0) + freq
                add[insert + pair[1]] = add.get(insert + pair[1], 0) + freq
                remove[pair] = remove.get(pair, 0) - freq
                elementcounter.update(freq * insert)

        paircounter.update(add) # outside loop to avoid dictionary size change during iteration error
        paircounter.update(remove)

    print(elementcounter, paircounter)
    print(elementcounter.most_common()[0][1] - elementcounter.most_common()[-1][1])


def main():
    template, instructions = inp()
    # partone(template, instructions)
    parttwo(template, instructions)
    print(time.time()-start)


main()
