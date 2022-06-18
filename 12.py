# --- Day 12: Passage Pathing ---
from collections import Counter
with open("12_input.txt") as f:
    rawinput = [line.replace("\n", "") for line in f.readlines()]


def partone():
    """Find number of paths which pass through small caves at most once"""
    paths = [["start"]]
    firstpath = True
    correctpaths = []

    for path in paths:
        for (ci, current) in enumerate(path):
            connected = []
            first = True # first valid entry in connected
            pathcopy = path[:]

            if current == "end":
                break
            if firstpath is False: # start at last index after first path
                if ci + 1 != len(path):
                    continue
            firstpath = False

            # building "connected"
            for entry in rawinput:
                if current in entry.split("-"): # prevents false positives e.g. end for d
                    connected.append(entry)

            # appending to paths from "connected"
            for ei, entry in enumerate(connected):
                entryb = entry.replace(current, "").replace("-", "") # remove current
                if entryb.islower(): # small cave
                    if entryb in path:
                        continue
                if first: # only the first valid index from "connected" is appended to path
                    path.append(entryb)
                    first = False
                else:
                    paths.append(pathcopy + [entryb])

    # removal of incomplete paths
    for path in paths:
        if path[-1] == "end":
            correctpaths.append(path)
    print(f"Part 1: There are {len(correctpaths)} paths.")


def parttwo():
    """Find number of paths when a single small cave can be visited twice"""
    paths = [["start"]]
    firstpath = True
    correctpaths = []

    for path in paths:
        pathvisitedtwice = False # single small cave can be visited twice
        smallcaves = []
        for (ci, current) in enumerate(path):
            connected = []
            first = True
            pathcopy = path[:]
            visitedtwice = False

            if current == "end":
                break
            if firstpath is False: # start at last index after first path
                if ci + 1 != len(path):
                    continue
            firstpath = False
            if pathvisitedtwice is False:  # check if pathvisitedtwice has been fufilled, then set to true
                smallcaves = [x for x in path if x.islower()]
                if Counter(smallcaves).most_common()[0][1] > 1:
                    pathvisitedtwice = True

            # building "connected"
            for entry in rawinput:
                if current in entry.split("-"): # prevents false positives if no split e.g. end for d
                    connected.append(entry)

            # appending to paths from "connected"
            for ei, entry in enumerate(connected):
                entryb = entry.replace(current, "").replace("-", "") # remove current

                if entryb.islower(): # small cave
                    if entryb == "start":
                        continue
                    if entryb in path:
                        if pathvisitedtwice is False:
                            if first and Counter(smallcaves + [entryb]).most_common()[0][1] > 1:
                                visitedtwice = True # visitedtwice is later converted to allow non-first entries
                        elif pathvisitedtwice:
                            continue
                if first:
                    path.append(entryb)
                    first = False
                else:
                    paths.append(pathcopy + [entryb])

            if visitedtwice:
                pathvisitedtwice = True

    # removal of incomplete paths
    for path in paths:
        if path[-1] == "end":
            correctpaths.append(path)
    print(f"Part 2: There are {len(correctpaths)} paths.")


def main():
    partone()
    parttwo()


if __name__ == "__main__":
    main()
