# --- Day 9: Smoke Basin ---
with open("input.txt") as f:
    rawinput = [[int(n) for n in line if n != "\n"] for line in f.readlines()]
print(rawinput)


def partone():
    """ Find low points """
    risklevel = []
    for ri, row in enumerate(rawinput):
        for ni, num in enumerate(row):

            # adjacent = [rawinput[ri-1][ni], rawinput[ri+1][ni], rawinput[ri][ni-1], rawinput[ri][ni+1]]
            adjacent = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if abs(x+y) == 1 and ri+x >= 0 and ni+y >= 0:

                        try:
                            adjacent.append(rawinput[ri+x][ni+y])
                        except IndexError:
                            continue

            lowpoint = True
            for value in adjacent:
                if num >= value:
                    lowpoint = False
            if lowpoint:
                risklevel.append(num+1)

    print(sum(risklevel))


# def parttwo():




if __name__ == "__main__":
    partone()
