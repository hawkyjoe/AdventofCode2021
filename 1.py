depthlist = []

while True:
    rawinput = input()
    if rawinput == "":
        break
    depthlist.append(int(rawinput)) # comparing strings with > does each character left to right therefore 976 !> 1004


def partone():
    increases = 0
    index = -1
    for depth in depthlist:
        if depth == depthlist[0]:
            index += 1
        else:
            index += 1
            before = depthlist[index-1]
            if depth > before:
                increases += 1
    print("Part 1:", increases)


def parttwo():
    increases = 0
    for i in range(len(depthlist)-3):
        if sum(depthlist[i+1:i+4]) > sum(depthlist[i:i+3]):
            increases += 1
    print("Part 2:", increases)


partone()
parttwo()
