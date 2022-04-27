# --- Day 4: Giant Squid ---
import numpy as np


def inp():
    """Input processing"""
    temp = []
    nestedboards = []

    with open("4_input.txt") as f:
        numberlist = f.readline().replace("\n", "").split(",")
        boardlist = f.read().split()
        if len(boardlist) % 25 == 0:
            for a in range(int(len(boardlist)/5)): # rows
                temp.append(list(boardlist[5*a:5*a+5]))
            for a in range(int(len(boardlist)/25)): # board
                nestedboards.append(list(temp[5*a:5*a+5]))
        else:
            print("fuck")
    return numberlist, boardlist, nestedboards


def partone(numberlist, boardlist):
    """First won bingo board"""
    for num in numberlist:
        for i in range(len(boardlist)):
            boardnumber = (i // 25)
            if num == boardlist[i]:
                boardlist[i] = "" # = boardlist[i].replace(boardlist[i], "")

            # checking rows for bingo
            checkingrow = boardlist[i-(i % 5):i+5-(i % 5)]
            if checkingrow == ["", "", "", "", ""]:
                return boardnumber, num

            # checking columns for bingo
            checkingcolumn = []
            for x in range(5):
                checkingcolumn.append(boardlist[25*boardnumber+(i % 5)+5*x])
                if checkingcolumn == ["", "", "", "", ""]:
                    return boardnumber, num


def partonecalc(boardlist, boardnumber, num):
    scorelist = boardlist[25 * boardnumber: 25 * boardnumber + 25]
    unmarked = sum([int(s) for s in scorelist if s != ""])
    print("Part 1\nWinning number:", num,
          "\nSum of unmarked numbers:", unmarked, "\nScore:", int(num) * unmarked)


def parttwo(numberlist, nestedboards):
    """Last won bingo board"""
    wonboards = []
    wondict = {}
    wonnum = 0

    for num in numberlist:
        for x in range(len(nestedboards)): # x is board
            for y in range(len(nestedboards[x])): # y is row
                for z in range(len(nestedboards[x][y])): # z is square
                    if num == str(nestedboards[x][y][z]):
                        nestedboards[x][y][z] = ""

                    checkingrow = nestedboards[x][y]
                    checkingcolumn = list(zip(*nestedboards[x])) # columns to rows
                    if checkingrow == ["", "", "", "", ""]:
                        if x not in wonboards:
                            wonboards.append(x)
                            wondict[x] = nestedboards[x]
                            wonnum = num
                            nestedboards[x] = np.zeros((5, 5)).tolist()

                    elif ("", "", "", "", "") in checkingcolumn:
                        if x not in wonboards:
                            wonboards.append(x)
                            wondict[x] = nestedboards[x]
                            wonnum = num
                            nestedboards[x] = np.zeros((5, 5)).tolist()

    unmarked = sum([int(w) for sublist in wondict[wonboards[-1]] for w in sublist if w != ""])
    print("Part 2\nWinning number:", wonnum,
          "\nSum of unmarked numbers:", unmarked, "\nScore:", unmarked * int(wonnum))


def main():
    numberlist, boardlist, nestedboards = inp()
    boardnumber, num = partone(numberlist, boardlist)
    partonecalc(boardlist, boardnumber, num)
    parttwo(numberlist, nestedboards)


if __name__ == "__main__":
    main()
