# --- Day 8: Seven Segment Search ---

def inp():
    signals = []
    outputs = []
    with open("8_input.txt") as file:
        rawinput = file.readlines()
        for line in rawinput:
            signals.append(line.replace("\n", "").partition("|")[0].strip(" ").split(" "))
            sortedsignals = [["".join(sorted(digit)) for digit in signal] for signal in signals]
            outputs.append(line.replace("\n", "").partition("|")[2].strip(" ").split(" "))
            sortedoutputs = [["".join(sorted(digit)) for digit in output] for output in outputs]
        return outputs, sortedsignals, sortedoutputs


def partone(outputs):
    """Count number of occurences of 1, 4, 7 or 8"""
    count = [0, 0, 0, 0] # [1, 4, 7, 8]
    for output in outputs:
        for digit in output:
            if len(digit) == 2: # one in seven segment form
                count[0] += 1
            elif len(digit) == 4: # four in seven segment form
                count[1] += 1
            elif len(digit) == 3: # seven in seven segment form
                count[2] += 1
            elif len(digit) == 7: # eight in seven segment form
                count[3] += 1
    print("Number of occurences of 1, 4, 7 and 8:", sum(count))


def parttwo(sortedsignals, sortedoutputs, outputs):
    """Determine values of outputs"""
    known = ["", "", "", "", "", "", "", "", "", ""]
    totalsum = 0
    for si, signal in list(enumerate(sortedsignals)):
        fivesegments = []
        sixsegments = []
        segmentcount = {}
        # sorting by number of segments
        for digit in signal:
            if len(digit) == 5: # 2, 3 or 5
                fivesegments.append(digit)
            elif len(digit) == 6: # 0, 6 or 9
                sixsegments.append(digit)
            else:
                if len(digit) == 2:
                    known[1] = digit
                elif len(digit) == 4:
                    known[4] = digit
                elif len(digit) == 3:
                    known[7] = digit
                elif len(digit) == 7:
                    known[8] = digit

            # finding 2, the only digit without f
            for segment in digit:
                segmentcount[segment] = segmentcount.get(segment, 0) + 1
        f = list(segmentcount.keys())[list(segmentcount.values()).index(9)] # get key with value
        segmentcount.clear()

        for digit in fivesegments:
            if f not in digit:
                known[2] = digit
                fivesegments.remove(digit)

        # finding 5, which contains segments b and f
        bf = "".join([char for char in known[8] if char not in known[2]]) # 8 - 2 leaves b and f
        b = bf.replace(f, "")
        for digit in fivesegments:
            if b in digit and f in digit:
                known[5] = digit
                fivesegments.remove(digit)

        # remaining digit is 3
        known[3] = fivesegments[0]

        # finding 0 which lacks segment d
        d = "".join([char for char in known[4] if char not in known[1]]).replace(b, "") # 4 - 1 = bd, bd - b = d
        for digit in sixsegments:
            if d not in digit:
                known[0] = digit
                sixsegments.remove(digit)

        # finding 6 which contains segment e
        e = "".join([char for char in known[2] if char not in known[3]]) # 4 - 2 - f = e
        for digit in sixsegments:
            if e in digit:
                known[6] = digit
                sixsegments.remove(digit)

        # remaining digit is 9
        known[9] = sixsegments[0]

        for di, digit in list(enumerate(sortedoutputs[si])): # si syncs output with signal
            for num in known:
                if num == digit:
                    outputs[si][di] = str(known.index(num))

    print("Outputs:", [int("".join(output)) for output in outputs])
    totalsum += sum([int("".join(output)) for output in outputs])
    print("Total sum:", totalsum)


def main():
    outputs, sortedsignals, sortedoutputs = inp()
    partone(outputs)
    parttwo(sortedsignals, sortedoutputs, outputs)


if __name__ == "__main__":
    main()
