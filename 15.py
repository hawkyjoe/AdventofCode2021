# --- Day 15: Chiton ---
with open("input.txt") as f:
    rawinput = [[int(x) for x in line if x != "\n"] for line in f.readlines()]

lastindex = len(rawinput)-1


def partone():
    paths = [[(rawinput[0][0], 0, 0)]]
    pathrisk = []
    firstpath = True
    for path in paths:
        print("next path")
        for pi, point in enumerate(path):
            if not firstpath:
                if pi + 1 != len(path):
                    continue
            value, ri, ci = point
            print(ri, ci)
            if (ri, ci) == (lastindex, lastindex): # endpoints are appended to nonfirsts
                print("path ended due to endpoint", path)
                continue
            pathcopy = path[:]
            first = True # first adjacent
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if abs(x + y) == 1 and ri + x >= 0 and ci + y >= 0:
                        try:
                            if (rawinput[ri + x][ci + y], ri + x, ci + y) not in path:  # prevent duplicates
                                if first:
                                    path.append((rawinput[ri + x][ci + y], ri + x, ci + y))
                                    first = False
                                    print("first", path)
                                    if (ri + x, ci + y) == (lastindex, lastindex):
                                        print("break inner")
                                        break
                                else:
                                    pathcopy2 = pathcopy[:] # consecutive nonfirsts issue
                                    pathcopy2.append((rawinput[ri + x][ci + y], ri + x, ci + y))
                                    paths.append(pathcopy2)
                                    print("nonfirst", pathcopy2)

                        except IndexError:
                            print("indexero")
                            continue
                else: # breaking out of multiple loops
                    continue
                print("break mid")
                break
            else:
                firstpath = False
                continue
            firstpath = False
            print("break outer")
            break

    print(paths)

    print(len(paths))
    # filter out paths without end
    paths = [path for path in paths if (rawinput[lastindex][lastindex], lastindex, lastindex) in path]

    # testing
    for path in paths:
        pathrisk.append(sum(list(zip(*path))[0]))
        if sum(list(zip(*path))[0]) == 7:
            print(path)

    pathrisk.sort()
    print(pathrisk)
    print(pathrisk[0])


partone()
