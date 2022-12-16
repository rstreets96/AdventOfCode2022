import numpy as np

###############################################################################
#Function to format the data after it's been read in
###############################################################################

def splitToLines(data):
    output = []
    for line in data:
        output.append(list(line.split()[0]))
    return(output)

###############################################################################
#Functions to complete part 1
###############################################################################

def circumference(rows, columns):
    total = len(rows[0]) * 2 + len(columns[0]) * 2 - 4
    return total

def visibleTreesInRow(row, columns, rowNum):
    sum = 0
    for i in range(1, len(row) - 1):
        visible = [True, True, True, True]
        currentTree = row[i]
        for tree in row[:i]:
            if(currentTree <= tree):
                visible[0] = False
                break
        for tree in row[i+1:]:
            if(currentTree <= tree):
                visible[1] = False
                break
        for tree in columns[i][:rowNum]:
            if(currentTree <= tree):
                visible[2] = False
                break
        for tree in columns[i][rowNum+1:]:
            if(currentTree <= tree):
                visible[3] = False
                break
        if(True in visible):
            sum += 1
    return sum
                
###############################################################################
#Function to complete part 2
###############################################################################

def scenicScores(row, columns, rowNum):
    output = []
    for i in range(0, len(row)):
        listLeft = row[:i]
        listLeft.reverse()
        #print(listLeft)
        listUp = columns[i][:rowNum]
        listUp.reverse()
        # print(listUp)
        # print('\r')
        count = [0, 0, 0, 0]
        currentTree = row[i]
        for tree in listLeft:
            count[0] += 1
            if(currentTree <= tree):
                break
        for tree in row[i+1:]:
            count[1] += 1
            if(currentTree <= tree):
                break
        for tree in listUp:
            count[2] += 1
            if(currentTree <= tree):
                break
        for tree in columns[i][rowNum+1:]:
            count[3] += 1
            if(currentTree <= tree):
                break
        #print(i)
        #print(count)
        output.append(count)
    return output

            
        
    


if __name__ == '__main__':
    fileObject = open("InputFiles/Day8.txt", "r")
    dataLines = fileObject.read().splitlines()
    
    rows = splitToLines(dataLines)
    columns = np.array(rows).T.tolist()

    #Part 1 Execution
    #############################################################
    # totSum = circumference(rows, columns)
    # for i in range(1, len(rows) - 1):
    #     totSum += visibleTreesInRow(rows[i], columns, i)
    # for i in range(1, len(rows) - 1):
    #     maxScenic = maxSecnicScoreInRow(rows[i], columns, i) 


    #Part 2 Execution
    #############################################################
    scores = []
    for i in range(0, len(rows)):
        scores.append(scenicScores(rows[i], columns, i)) 
    maxScore = 0
    for set in scores:
        for score in set:
            value = score[0] * score[1] * score[2] * score[3]
            if(value > maxScore):
                maxScore = value
    print(maxScore)
    
   
