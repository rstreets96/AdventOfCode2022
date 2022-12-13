def linesToInputs(data):
    output = [[]]
    output = [line.split(' ') for line in data]
    return output

def pointsWon(data):
    lookUpWin = {'A':{'X':4, 'Y':8, 'Z':3}, 'B':{'X':1, 'Y':5, 'Z':9}, 'C':{'X':7, 'Y':2, 'Z':6}}
    points = 0
    for game in data:
        points += lookUpWin[game[0]][game[1]]
    return points

def pickMyInput(data):
    lookUpInput = {'A':{'X':'Z', 'Y':'X', 'Z':'Y'}, 'B':{'X':'X', 'Y':'Y', 'Z':'Z'}, 'C':{'X':'Y', 'Y':'Z', 'Z':'X'}}
    output = []
    for game in data:
        game[1] = lookUpInput[game[0]][game[1]]
        output.append(game)
    return output


fileObject = open("InputFiles/Day2.txt", "r")
dataLines = fileObject.read().splitlines()
inputs = linesToInputs(dataLines)
newInputs = pickMyInput(inputs)
points = pointsWon(newInputs)
print(points)