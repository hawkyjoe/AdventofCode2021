# --- Day 5: Hydrothermal Venture ---
def inp():
    """Input processing"""
    before = []
    after = []

    with open("input_05.txt") as f:
        rawinput = f.readlines()
        for line in rawinput:
            temp = line.replace(" ", "").replace("\n", "").rpartition("->")
            before.append(tuple(temp[0].split(",")))
            after.append(tuple(temp[2].split(",")))

    intbefore = [tuple(int(x) for x in tup) for tup in before]
    intafter = [tuple(int(x) for x in tup) for tup in after]
    return intbefore, intafter


def partone(intbefore, intafter):
    """Number of coordinates which occur more than twice (horizontal and vertical lines)"""
    hvbefore = []
    hvafter = []
    coordcount = {}

    for i in range(len(intbefore)): # filter out diagonal leaving horizontal/vertical
        if intbefore[i][0] == intafter[i][0] or intbefore[i][1] == intafter[i][1]:
            hvbefore.append(intbefore[i])
            hvafter.append(intafter[i])

    for i in range(len(hvbefore)):
        tempcoord = []
        xdiff = abs(hvbefore[i][0] - hvafter[i][0])
        ydiff = abs(hvbefore[i][1] - hvafter[i][1])

        if xdiff != 0: # horizontal (Δx)
            ystatic = hvbefore[i][1]
            xlow = min(hvbefore[i][0], hvafter[i][0])
            for j in range(xdiff + 1):
                tempcoord.append((xlow + j, ystatic))
            for coord in tempcoord:
                coordcount[coord] = coordcount.get(coord, 0) + 1 # to count with dict while adding new key

        elif ydiff != 0: # vertical (Δy)
            xstatic = hvbefore[i][0]
            ylow = min(hvbefore[i][1], hvafter[i][1])
            for j in range(ydiff + 1):
                tempcoord.append((xstatic, ylow + j))
            for coord in tempcoord:
                coordcount[coord] = coordcount.get(coord, 0) + 1

    return coordcount


def parttwo(intbefore, intafter, coordcount):
    """Number of coordinates which occur more than twice (diagonal)"""
    dbefore = []
    dafter = []

    for i in range(len(intbefore)):  # filter out diagonal leaving horizontal/vertical
        if abs(intbefore[i][0] - intafter[i][0]) == abs(intbefore[i][1] - intafter[i][1]):
            dbefore.append(intbefore[i])
            dafter.append(intafter[i])

    for i in range(len(dbefore)):
        tempcoord = []
        diff = abs(dbefore[i][0] - dafter[i][0])
        xlow, ylow = min(dbefore[i][0], dafter[i][0]), min(dbefore[i][1], dafter[i][1])
        yhigh = max(dbefore[i][1], dafter[i][1])

        if (dbefore[i][1] - dafter[i][1])/(dbefore[i][0] - dafter[i][0]) > 0: # positive gradient
            for j in range(diff + 1):
                tempcoord.append((xlow + j, ylow + j))
            for coord in tempcoord:
                coordcount[coord] = coordcount.get(coord, 0) + 1

        elif (dbefore[i][1] - dafter[i][1])/(dbefore[i][0] - dafter[i][0]) < 0: # negative gradient
            for j in range(diff + 1):
                tempcoord.append((xlow + j, yhigh - j))
            for coord in tempcoord:
                coordcount[coord] = coordcount.get(coord, 0) + 1

    return coordcount


def main():
    intbefore, intafter = inp()
    coordcount = partone(intbefore, intafter)
    coordvalues = coordcount.values()
    dangerous = [x for x in coordvalues if x >= 2]
    print("Overlapping coordinates without diagonals:", len(dangerous))

    parttwo(intbefore, intafter, coordcount)
    coordvalues = coordcount.values()
    dangerous = [x for x in coordvalues if x >= 2]
    print("Overlapping coordinates with diagonals:", len(dangerous))


main()
