# --- Day 7: The Treachery of Whales ---
with open("input_07.txt") as f:
    rawinput = f.readline().split(",")
    hcoords = [int(x) for x in rawinput]


def test1():
    """Position closest to all valuves (brute force part 1)"""
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
    """Position closest to all values with triangular number steps (brute force part 2)"""
    fuel = 0
    position = False
    for i in range(max(hcoords)):
        currentfuel = 0
        for coord in hcoords:
            distance = abs(coord - i)
            currentfuel += (distance * (distance + 1))/2 # triangular number formula
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


if __name__ == "__main__":
    main()
