###############################################################################
#Function used for Part 1
###############################################################################

def runCycles(cmds):
    xValue = 1
    cycleCount = 0
    sigStrenSum = 0
    importantCycles = [20, 60, 100, 140, 180, 220]
    for cmd in cmds:
        if(cmd[0] == 'addx'):
            cycleCount += 1   
            if(cycleCount in importantCycles):
                sigStrenSum += cycleCount * xValue   
            cycleCount += 1   
            if(cycleCount in importantCycles):
                sigStrenSum += cycleCount * xValue       
            xValue += int(cmd[1])
        elif(cmd[0] == 'noop'):
            cycleCount += 1
            if(cycleCount in importantCycles):
                sigStrenSum += cycleCount * xValue
    return xValue, cycleCount, sigStrenSum

###############################################################################
#Function used for Part 2
###############################################################################
def printScreen(cmds):
    xValue = 1
    cycleCount = 0
    pixels = [[], [], [], [], [], []]
    row = 0
    for cmd in cmds:
        if(cmd[0] == 'addx'):
            printPixel(cycleCount, xValue, pixels, row)
            cycleCount, row = incrementCycle(cycleCount, row)   
            printPixel(cycleCount, xValue, pixels, row)
            cycleCount, row = incrementCycle(cycleCount, row)            
            xValue += int(cmd[1])
        elif(cmd[0] == 'noop'):
            printPixel(cycleCount, xValue, pixels, row)
            cycleCount, row = incrementCycle(cycleCount, row)
            
    return pixels

def printPixel(cursor, xValue, pixels, row):
    if(cursor == xValue - 1 or cursor == xValue + 1 or cursor == xValue):
        pixels[row].append('#')
    else:
        pixels[row].append('.')

def incrementCycle(cycleCount, row):
    cycleCount += 1
    if(cycleCount > 39):
        cycleCount = 0
        row += 1
    return cycleCount, row



if __name__ == '__main__':
    fileObject = open("InputFiles/Day10.txt", "r")
    dataLines = fileObject.read().splitlines()
    cmds = []
    for line in dataLines:
        cmds.append(line.split(' '))

    pixels = printScreen(cmds)

    for row in pixels:
        print(''.join(row))
