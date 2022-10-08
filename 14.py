# --- Day 14: Extended Polyermization ---
from collections import Counter

pairinsertion = []

with open("input_14.txt") as f:
    template = f.readline().replace("\n", "")
    for line in f.readlines():
        if line != "\n":
            pairinsertion.append(tuple(line.replace("\n", "").split(" -> ")))


def partone():
    nexttemplate = list(template)
    pairs = (list(zip(*pairinsertion))[0])

    for n in range(10):
        toinsert = []
        for i, x in enumerate(nexttemplate):
            if i == 0:
                continue
            for pi, pair in enumerate(pairs):
                if nexttemplate[i-1] + x == pair:
                    toinsert.append((i, pairinsertion[pi][1]))

        # print(n, "to insert", toinsert) # insert at i

        for yi, y in (reversed(toinsert)):
            nexttemplate.insert(yi, y)

        # print("end step", n, nexttemplate)
    print(Counter(nexttemplate).most_common()[0][1] - Counter(nexttemplate).most_common()[-1][1])


partone()
