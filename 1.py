# --- Day 1: Sonar Sweep ---


def read_default_input():
    strs_input = open("1_input.txt", "r").readlines()
    return [int(string) for string in strs_input]
    

def partone(depthlist):
    """Counts number of times the depth measurement (input) increases from previous value"""
    increases = 0
    for i in range(len(depthlist)-1):
        curr_val, next_val = depthlist[i], depthlist[i+1]
        if next_val > curr_val:
            increases += 1
    print("Part 1:", increases)


def parttwo(depthlist):
    """Counts number of times the depth measurement (input) increases in 3-measurement sliding window"""
    increases = 0
    for i in range(len(depthlist)-3):
        if sum(depthlist[i+1:i+4]) > sum(depthlist[i:i+3]):
            increases += 1
    print("Part 2:", increases)


partone(read_default_input())
parttwo(read_default_input())
