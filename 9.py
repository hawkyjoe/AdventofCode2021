# --- Day 9: Smoke Basin ---
with open("input.txt") as f:
    rawinput = [[int(n) for n in line if n != "\n"] for line in f.readlines()]


def partone():
    """Find low points"""
    lowpoints = []
    risklevel = []
    for ri, row in enumerate(rawinput):
        for ci, num in enumerate(row):
            # adjacents = [rawinput[ri-1][ci], rawinput[ri+1][ci], rawinput[ri][ci-1], rawinput[ri][ci+1]]
            adjacents = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if abs(x+y) == 1 and ri+x >= 0 and ci+y >= 0:
                        try:
                            adjacents.append(rawinput[ri+x][ci+y])
                        except IndexError:
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
    """Scan around lowpoints for non 9 heights"""
    basinsizes = []

    for lowpoint in lowpoints:
        adjacents = [lowpoint]
        for adjacent in adjacents:
            ri, ci = adjacent
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if abs(x + y) == 1 and ri + x >= 0 and ci + y >= 0:
                        try:
                            if rawinput[ri + x][ci + y] != 9 and (ri+x, ci+y) not in adjacents:
                                adjacents.append((ri+x, ci+y))
                        except IndexError:
                            continue
        basinsizes.append(len(adjacents))
    basinsizes.sort(reverse=True)
    print(f"Three largest basins: {basinsizes[0]} * {basinsizes[1]} * {basinsizes[2]} = {basinsizes[0] * basinsizes[1] * basinsizes[2]}")


if __name__ == "__main__":
    lowpointlist = partone()
    parttwo(lowpointlist)
