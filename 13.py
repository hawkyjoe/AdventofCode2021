# --- Day 13: Transparent Origami ---
import matplotlib.pyplot as plt


def inp():
    """Input processing"""
    coords = []
    instructions = []
    with open("input_13.txt") as f:
        for line in f.readlines():
            if "," in line:
                coords.append([int(x) for x in line.replace("\n", "").split(",")])
            elif "fold" in line:
                instruction = line.replace("\n", "").replace("fold along ", "").split("=")
                instructions.append(tuple([instruction[0], int(instruction[1])]))
    return coords, instructions


def partone(coords, instructions):
    """Prints number of dots remaining after the first fold instructions"""
    foldaxis, foldvalue = instructions[0]
    if foldaxis == "x": # fold left
        index = 0
    else: # fold up
        index = 1

    tofold = [coord for coord in coords if coord[index] > foldvalue]
    remaining = [coord for coord in coords if coord[index] <= foldvalue]

    for coord in tofold:
        coord[index] = foldvalue - (coord[index] - foldvalue)

    folded = [tuple(x) for x in tofold + remaining] # lists are unhashable (mutable) and unable to be converted to sets
    folded = list(set(folded)) # remove duplicates
    print(f"There are {len(folded)} dots remaining after the first fold instructions.")


def parttwo(coords, instructions):
    """Plots graph showing result of all fold instructions (8 capital letters)"""
    folded = coords

    for instruction in instructions:
        foldaxis, foldvalue = instruction
        if foldaxis == "x":  # fold left
            index = 0
        else:  # fold up
            index = 1

        tofold = [list(coord) for coord in folded if coord[index] > foldvalue]
        remaining = [list(coord) for coord in folded if coord[index] <= foldvalue]

        for coord in tofold:
            coord[index] = foldvalue - (coord[index] - foldvalue)

        folded = [tuple(x) for x in tofold + remaining]
        folded = list(set(folded))

    x, y = zip(*folded)
    plt.scatter(x, y)
    ax = plt.gca()
    ax.invert_yaxis() # invert axis required to show letters flipped correctly
    plt.subplots_adjust(top=0.25) # plot subplot params adjusted to show letters more clearly
    plt.show()


def main():
    coords, instructions = inp()
    partone(coords, instructions)
    parttwo(coords, instructions)


main()
