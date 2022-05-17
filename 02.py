# --- Day 2: Dive! ---
horizontallist = []
depthlist = []
bothlist = []

while True:
    rawinput = input()
    if rawinput == "":
        break
    bothlist.append(rawinput)
    temp = rawinput.split()
    if temp[0] == "forward":
        horizontallist.append(int(temp[1]))
    elif temp[0] == "down":
        depthlist.append(int(temp[1]))
    elif temp[0] == "up":
        depthlist.append(-1 * int(temp[1]))


def partone():
    """Calculate horizontal position and depth"""
    horizontal = sum(horizontallist)
    depth = sum(depthlist)
    print("Part 1:", horizontal * depth)


def parttwo():
    """Calculate horizontal position and depth considering aim value"""
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(bothlist)):
        if "down" in bothlist[i]:
            splitboth = bothlist[i].split()
            aim += int(splitboth[1])
        elif "up" in bothlist[i]:
            splitboth = bothlist[i].split()
            aim -= int(splitboth[1])
        elif "forward" in bothlist[i]:
            splitboth = bothlist[i].split()
            horizontal += int(splitboth[1])
            depth += aim * int(splitboth[1])
    print("Part 2:", horizontal * depth)


partone()
parttwo()
