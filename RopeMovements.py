###############################################################################
#Class used to hold a coordinate pair
###############################################################################
class CoordPosition():
    def __init__(self, x, y):
        self.x = x
        self.y = y

###############################################################################
#Function to handle one line of movement input
###############################################################################

def doOneMoveSet(moveSet, head, tail):
    direction = 0
    up = 1
    down = 2
    left = 3
    right = 4
    tailMoves = {-2:{-2:[-1, -1], -1:[-1, -1], 0:[-1, 0], 1:[-1, 1], 2:[-1, 1]}, 
                -1:{-2:[-1, -1], -1:[0, 0], 0:[0, 0], 1:[0, 0], 2:[-1, 1]}, 
                0:{-2:[0, -1], -1:[0, 0], 0:[0, 0], 1:[0, 0], 2:[0, 1]}, 
                1:{-2:[1, -1], -1:[0, 0], 0:[0, 0], 1:[0, 0], 2:[1, 1]}, 
                2:{-2:[1, -1], -1:[1, -1], 0:[1, 0], 1:[1, 1], 2:[1, 1]}}

    if(moveSet[0] == 'U'):
        direction = up
    elif(moveSet[0] == 'D'):
        direction = down
    elif(moveSet[0] == 'L'):
        direction = left
    elif(moveSet[0] == 'R'):
        direction = right   
    for i in range(0, int(moveSet[1])):
        if(direction == up):
            head.y += 1
        elif(direction == down):
            head.y -= 1
        elif(direction == left):
            head.x -= 1
        elif(direction == right):
            head.x += 1
        yDiff = head.y - tail.y
        xDiff = head.x - tail.x

        tail.x += tailMoves[xDiff][yDiff][0]
        tail.y += tailMoves[xDiff][yDiff][1]

        tailSpot = CoordPosition(tail.x, tail.y)
        newSpot = True
        for tailPos in tailPosList:
            if((tailPos.x == tailSpot.x) and (tailPos.y == tailSpot.y)):
                newSpot = False
        if(newSpot):
            tailPosList.append(tailSpot)
    return(head, tail)

###############################################################################
#Global Variable to hold all unique Tail coordinates
###############################################################################

tailPosList = []

if __name__ == '__main__':
    fileObject = open("InputFiles/Day9.txt", "r")
    dataLines = fileObject.read().splitlines()
    moves = []
    for line in dataLines:
        moves.append(line.split(' '))

###############################################################################
#Execution for Part 1
###############################################################################

    headPos = CoordPosition(0, 0)
    tailPos = CoordPosition(0, 0)
    for move in moves:
        headPos, tailPos = doOneMoveSet(move, headPos, tailPos)

    print(len(tailPosList))


