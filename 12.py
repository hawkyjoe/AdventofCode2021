# --- Day 12: Passage Pathing ---
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

            if firstpath is False: # start at last index after first path
                if ci + 1 != len(path):
                    continue
            if current == "end":
                break

            for entry in rawinput:
                if current in entry.split("-"): # prevents false positives if no split e.g. end for d
                    connected.append(entry)
            pathcopy = path[:]
            previous = ""
            first = True

            if path[-1].isupper(): # big cave, first will always be start and therefore false
                previous = path[-2]

            for entry in connected:
                entryb = entry.replace(current, "").replace("-", "") # remove current

                if entryb.islower(): # small cave
                    if entryb in path:
                        continue

                if entryb == previous: # before and after big cave cannot be the same or infinite loop
                    continue

                if first:
                    path.append(entryb)
                    first = False
                else:
                    paths.append(pathcopy + [entryb])

        firstpath = False

    for path in paths:
        if path[-1] == "end":
            correctpaths.append(path)
    print(f" There are {len(correctpaths)} paths.")


partone()
