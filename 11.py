# --- Day 11: Dumbo Octopus ---
import numpy as np


def inp():
    """Input processing"""
    with open("11_input.txt") as f:
        rawinput = [[int(n) for n in line if n != "\n"] for line in f.readlines()]
    return np.array(rawinput)


def partone(npgrid):
    """Count number of flashes over 100 days"""
    flashes = 0

    for n in range(100): # steps
        npgrid = npgrid + 1
        while np.any(npgrid > 9):
            unflashed = np.array(npgrid > 9).nonzero() # returns indices of npgrid == 0, same as np.where(condition)
            npgrid = np.where(npgrid > 9, 0, npgrid)
            unflashed = np.transpose(unflashed).tolist()
            for index in unflashed:
                ri, ci = index
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if not x == y == 0: # adjacent + diagonals
                            if 0 <= ri + x <= 9 and 0 <= ci + y <= 9: # handling index errors
                                if npgrid[ri+x][ci+y] != 0: # cannot flash more than once and flashes at end of step
                                    npgrid[ri+x][ci+y] += 1

        flashes += np.count_nonzero(npgrid == 0)

    print(f"Flashes after 100 steps: {flashes}")


def parttwo(npgrid):
    """Find step at which all octopuses flash together"""
    flashes = 0
    step = 0

    while True:
        step += 1
        npgrid = npgrid + 1
        while np.any(npgrid > 9):
            unflashed = np.array(npgrid > 9).nonzero()  # returns indices of npgrid == 0, same as np.where(condition)
            npgrid = np.where(npgrid > 9, 0, npgrid)
            unflashed = np.transpose(unflashed).tolist()
            for index in unflashed:
                ri, ci = index
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if not x == y == 0:  # adjacent + diagonals
                            if 0 <= ri + x <= 9 and 0 <= ci + y <= 9:  # handling index errors
                                if npgrid[ri+x][ci+y] != 0:  # cannot flash more than once and flashes at end of step
                                    npgrid[ri+x][ci+y] += 1

        flashes += np.count_nonzero(npgrid == 0)
        if np.count_nonzero(npgrid == 0) == 100:
            print(f"Step of first occurence of simultaneous flashing: {step}")
            return


def main():
    npgrid = inp()
    partone(npgrid)
    parttwo(npgrid)


if __name__ == "__main__":
    main()
