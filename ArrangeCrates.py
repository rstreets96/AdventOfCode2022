import numpy as np

def parsingStartPositions(data):
    output = []
    for line in data:        
        if(line == ' 1   2   3   4   5   6   7   8   9 '):
            break
        line = [line[i:i+3] for i in range(0, len(line), 4)]
        output.append(line)
    return output

def rowsToColumns(data):
    transposed = np.array(data).T.tolist()
    for line in transposed:
        line.reverse()
        while '   ' in line:
            line.remove('   ')
    return transposed

def parsingMoves(data):
    output = []
    startMoves = False
    for line in data:
        if(not startMoves):
            if(line == ''):
                startMoves = True
            else:
                continue
        else:
            output.append(line.split(' '))
    return output

###############################################################################
#Part One Functions
###############################################################################
def move1Crate(positionData, startColumn, endColumn):
    positionData[endColumn].append(positionData[startColumn][-1])
    positionData[startColumn].pop(-1)

def moveCrates(positionData, move):
    numMoves = int(move[1])
    startColumn = int(move[3]) - 1
    endColumn = int(move[5]) - 1
    for move in range(0, numMoves):
        move1Crate(positionData, startColumn, endColumn)

###############################################################################
#Part Two Functions
###############################################################################
def moveMultipleCrates(positionData, move):
    numCrates = int(move[1])  
    startColumn = int(move[3]) - 1
    endColumn = int(move[5]) - 1
    positionData[endColumn].extend(positionData[startColumn][-numCrates:])
    del positionData[startColumn][-numCrates:]

###############################################################################
#Main Execution
###############################################################################
if __name__ == '__main__':
    fileObject = open("InputFiles/Day5.txt", "r")
    dataLines = fileObject.read().splitlines()
    startPositions = parsingStartPositions(dataLines)
    columns = rowsToColumns(startPositions)
    moves = parsingMoves(dataLines)
    for move in moves:
        moveMultipleCrates(columns, move)
    for line in columns:
        print(line)