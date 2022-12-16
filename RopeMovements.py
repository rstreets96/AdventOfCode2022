

if __name__ == '__main__':
    fileObject = open("InputFiles/Day9.txt", "r")
    dataLines = fileObject.read().splitlines()
    moves = []
    for line in dataLines:
        moves.append(line.split(' '))

    originShiftx = 0
    originShifty = 0

    for move in moves:
        print(move)
