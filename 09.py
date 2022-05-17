# --- Day 9: Smoke Basin ---
with open("input_09.txt") as f:
    rawinput = [[int(n) for n in line if n != "\n"] for line in f.readlines()]


def partone():
    """Checks if adjacent values are smaller, until lowpoint is found with all adjacent values greater"""
    lowpoints = []
    risklevel = []
    for ri, row in enumerate(rawinput):
        for ci, num in enumerate(row):
            # adjacents = [rawinput[ri-1][ci], rawinput[ri+1][ci], rawinput[ri][ci-1], rawinput[ri][ci+1]]
            adjacents = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if abs(x+y) == 1 and ri+x >= 0 and ci+y >= 0: # if +/-1 in x and y (adjacent cells)
                        # ri/ci + x/y >= 0 prevents negative indices which do not result in index error
                        try:
                            adjacents.append(rawinput[ri+x][ci+y])
                        except IndexError: # index error occurs at edge of grid where there are no adjacent values
                            # only caught if greater than size, i.e. can be avoided with ri/ci +x/y <= row/col length
                            continue
            lowpoint = True
            for value in adjacents:
                if num >= value:
                    lowpoint = False
            if lowpoint:
                risklevel.append(num+1)
                lowpoints.append((ri, ci))

    print("Sum of Risk Levels:", sum(risklevel))
    return lowpoints


def parttwo(lowpoints):
    """Scan around lowpoints for non 9 heights until no more values can be counted"""
    basinsizes = []

    for lowpoint in lowpoints:
        adjacents = [lowpoint]
        for adjacent in adjacents:
            ri, ci = adjacent
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if abs(x + y) == 1 and ri + x >= 0 and ci + y >= 0:
                        try:
                            if rawinput[ri + x][ci + y] != 9 and (ri+x, ci+y) not in adjacents: # prevent duplicates
                                adjacents.append((ri+x, ci+y))
                        except IndexError:
                            continue
        basinsizes.append(len(adjacents))
    basinsizes.sort(reverse=True)
    print(f"Three largest basins: {basinsizes[0]} * {basinsizes[1]} * {basinsizes[2]} = {basinsizes[0] * basinsizes[1] * basinsizes[2]}")


def main():
    lowpoints = partone()
    parttwo(lowpoints)


if __name__ == "__main__":
    main()
