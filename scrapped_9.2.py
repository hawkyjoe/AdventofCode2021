import numpy as np
from collections import defaultdict

with open("input.txt") as f:
    rawinput = [[int(n) for n in line if n != "\n"] for line in f.readlines()]

rowcount = len(rawinput)
columncount = len(rawinput[0])
npboard = np.array(rawinput)
heightmap = np.full((rowcount+2, columncount+2), 9) # adding border of 9s to enclose basins ending at edges
heightmap[1:rowcount+1, 1:columncount+1] = npboard


def parttwo():
    """ Initiate basin search """
    basinsizes = []
    print(heightmap)
    for xi, x in np.ndenumerate(heightmap):
        columnindices = defaultdict(list)
        (xrow, xcolumn) = xi
        if x == 9 or x == 10:
            continue
        else:
            print("Basin found beginning:", xi)
            columnindices[xrow].append(xcolumn)
            basin = checkrow(xrow, columnindices, True)
            basinsizes.append(basin)

    print("END")
    basinsizes.sort(reverse=True)
    print(basinsizes)
    if len(basinsizes) > 3:
        print("ANSWER:", basinsizes[0] * basinsizes[1] * basinsizes[2])


def checkrow(row, columnindices, first=False):
    """ Check each row for connected non 9s until basin is found """
    column = columnindices[row][0]

    if first is True:
        columnindices[row] = []
    else:
        row += 1
        # check left
        for index, height in np.ndenumerate(heightmap[row][column::-1]):
            (diff,) = index # diff is index of loop slice
            correctedindex = column - diff
            if height == 9:
                break
            elif height == 10:
                print("branch error")
            elif height < 9:
                if diff == 0:
                    continue
                else:
                    columnindices[row].insert(0, correctedindex)
                    heightmap[row][correctedindex] = 10

    # check right
    for index, height in np.ndenumerate(heightmap[row][column:]):
        (diff,) = index
        correctedindex = diff + column
        if height == 9:
            # 9 mid-row, if first, row - 1 will not work and case will be caught by branch()
            if first is False and correctedindex < max(columnindices[row-1]):
                print("midrow continue", row, correctedindex, max(columnindices[row-1]))
                continue
            else:
                print("check next row arguments", row, columnindices)
                break
        elif height == 10:
            print("branch error")
        elif height < 9:
            # check index is connected to basin, if first is True, 9 mid-row will not occur
            if first is False and correctedindex not in columnindices[row-1]:
                if heightmap[row][correctedindex-1] == 9 and heightmap[row][correctedindex+1] == 9:
                    print("disconnected", row, correctedindex)
                    continue
            columnindices[row].append(correctedindex)
            heightmap[row][correctedindex] = 10

    # check for branches
    if first is False:
        leftbranch = [x for x in columnindices[row] if x < min(columnindices[row - 1])-1]
        rightbranch = [x for x in columnindices[row] if x > max(columnindices[row - 1])+1]
        if len(leftbranch) > 0 or len(rightbranch) > 0:
            columnindices = branch(row, leftbranch, rightbranch, columnindices)

    # check if basin is found
    if len(columnindices[row]) == 0:
        print("Basin found")
        basinsize = len([x for sublist in columnindices.values() for x in sublist]) # unpack nested lists
        print("Basin size:", basinsize)
        print(heightmap)
        return basinsize

    return checkrow(row, columnindices)


def branch(row, leftbranch, rightbranch, columnindices):
    """ Check for edge case where basin extends horizontally past previous row and returns to it """
    print("branch", leftbranch)

    for branchindex in leftbranch[::-1]:
        for yindex, y in np.ndenumerate(heightmap[row - 1::-1, branchindex]): # multiple index slice of outer req. [,]
            (rowdiff,) = yindex
            correctedrow = row - 1 - rowdiff
            branchrow = []
            if y == 9 or y == 10:
                # go to min of minnest branch
                break
            elif y < 9:
                for xindex, x in np.ndenumerate(heightmap[correctedrow][branchindex::-1]):
                    (diff,) = xindex
                    correctedindex = branchindex - diff
                    if x == 9 or x == 10:
                        if correctedindex > min(leftbranch):
                            print("branch midrow continue")
                            continue
                        else:
                            branchrow.extend(columnindices[correctedrow])
                            columnindices[correctedrow] = branchrow
                            print("row END", correctedrow, columnindices[correctedrow])
                            break
                    elif x < 9:
                        branchrow.insert(0, correctedindex)
                        heightmap[correctedrow][correctedindex] = 10
                        print("branchrow", branchrow, correctedrow, correctedindex)

                print("row end")
                # if min branchrow < row below, check row below till min
    return columnindices


parttwo()
