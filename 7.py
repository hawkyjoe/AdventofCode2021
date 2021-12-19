with open("day 7 input.txt") as f:
    rawinput = f.readline().split(",")
    hcoords = [int(x) for x in rawinput]


def test1():
    """Brute force part 1"""
    fuel = 0
    position = False
    for i in range(max(hcoords)):
        currentfuel = 0
        for coord in hcoords:
            distance = abs(coord - i)
            currentfuel += distance
        if fuel != 0:
            if currentfuel < fuel:
                fuel = currentfuel
                position = i
        else:
            fuel = currentfuel
    print(fuel, position)


def partone():
    """Sum of distance from each position to median"""
    hcoords.sort()
    if len(hcoords) % 2 == 0:
        median = (hcoords[int(len(hcoords)/2)] + hcoords[int(len(hcoords)/2)])/2
    else:
        median = hcoords[int(len(hcoords)-1/2)]
    fuel = 0
    for coord in hcoords:
        fuel += abs(median - coord)
    print("Median:", median, "Fuel used (distance):", fuel)


def test2():
    """Brute force part 2, mean doesn't work lol"""
    fuel = 0
    position = False
    for i in range(max(hcoords)):
        currentfuel = 0
        for coord in hcoords:
            distance = abs(coord - i)
            currentfuel += (distance * (distance + 1))/2 # triangular numbers
        if fuel != 0:
            if currentfuel < fuel:
                fuel = currentfuel
                position = i
        else:
            fuel = currentfuel
    print("Position:", position, "Fuel used (distance):", fuel)


def main():
    partone()
    test2()


main()