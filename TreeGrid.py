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
                

                

if __name__ == '__main__':
    fileObject = open("InputFiles/Day8.txt", "r")
    dataLines = fileObject.read().splitlines()
    
    rows = splitToLines(dataLines)
    columns = np.array(rows).T.tolist()

    totSum = circumference(rows, columns)
    for i in range(1, len(rows) - 1):
        totSum += visibleTreesInRow(rows[i], columns, i)
    print(totSum)
    
   
