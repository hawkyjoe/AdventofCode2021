# doesn't work if all are removed during same (mostcommon[1] == leastcommon[1])
from collections import Counter

binarylist = []

while True:
    rawinput = input()
    if rawinput == "":
        break
    binarylist.append(rawinput)


def partone():
    gammarate = ""
    epsilonrate = ""
    for i in range(len(binarylist[0])):
        position = [] # holds characters for bit position i
        dictionary = {"0": 0, "1": 0}
        for binary in binarylist:
            position.append(binary[i])
        for num in position:
            if num == "0":
                dictionary["0"] += 1
            elif num == "1":
                dictionary["1"] += 1
        sort = sorted(dictionary, key=dictionary.get) # sorted based on value of key function
        gammarate += str(sort[1]) # most common
        epsilonrate += str(sort[0]) # least common

    print("Power consumption (epsilonrate * gammarate):", int(gammarate, 2) * int(epsilonrate, 2))


def parttwo():
    oxygengenerator = binarylist[:] # oxygen generator keeps most common value or 1 if equal
    co2scrubber = binarylist[:] # co2 scrubber keeps least common value or 0 if equal

# oxygengenerator
    for i in range(len(binarylist[0])):
        position = []
        if len(oxygengenerator) == 1:
            break

        for binary in oxygengenerator:
            position.append(binary[i])
        mostcommon = Counter(position).most_common()[0]
        leastcommon = Counter(position).most_common()[-1]

        if mostcommon[1] == leastcommon[1]:
            for index1, binary1 in reversed(list(enumerate(oxygengenerator))): # avoids range error with pop, index
                if binary1[i] == "0":
                    oxygengenerator.pop(index1)
            continue

        for index, binary in reversed(list(enumerate(oxygengenerator))):
            if binary[i] == leastcommon[0]:
                oxygengenerator.pop(index) # keep most common (oxygen generator rating)

# co2scrubber
    for i in range(len(binarylist[0])):
        position = []
        if len(co2scrubber) == 1:
            break

        for binary in co2scrubber:
            position.append(binary[i])
        mostcommon = Counter(position).most_common()[0]
        leastcommon = Counter(position).most_common()[-1]

        if mostcommon[1] == leastcommon[1]:
            for index1, binary1 in reversed(list(enumerate(co2scrubber))):
                if binary1[i] == "1":
                    co2scrubber.pop(index1)
            continue

        for index, binary in reversed(list(enumerate(co2scrubber))):
            if binary[i] == mostcommon[0]:
                co2scrubber.pop(index) # keep most common (oxygen generator rating)

    print("Life support rating (oxygen * co2):", int(oxygengenerator[0], 2) * int(co2scrubber[0], 2))


partone()
parttwo()
