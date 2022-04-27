# --- Day 6: Lanternfish ---
def inp():
    with open("6_input.txt") as f:
        rawinput = f.readline().split(",")
        fishlist = [int(x) for x in rawinput]
    return fishlist


def partone(fishlist):
    """Calculates exponential growth of fish (tracking each fish)"""
    days = 18
    fishtimers = fishlist[:]
    for day in range(days):
        for i in range(len(fishtimers)):
            fishtimers[i] -= 1
            if fishtimers[i] == -1:
                fishtimers.append(8)
                fishtimers[i] = 6

    print("Number of fish after {} days:".format(days), len(fishtimers))


def parttwo(fishlist):
    """Calculates exponential growth of fish (tracking age of fish)"""
    days = 256
    fishtimers = [] # ages: [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, buffer], age = index - 1

    # initialize fishtimers
    for i in range(11):
        fishtimers.append(0)
    for fishage in fishlist:
        fishtimers[fishage+1] += 1

    for day in range(days):
        for i in range(10):
            fishtimers[i] = fishtimers[i+1]
        for i in range(10):
            if i == 0:
                fishtimers[7] += fishtimers[0]
                fishtimers[9] += fishtimers[0]
                fishtimers[0] = 0

    print("Number of fish after {} days:".format(days), sum(fishtimers))


def main():
    fishlist = inp()
    partone(fishlist)
    parttwo(fishlist)


if __name__ == "__main__":
    main()
