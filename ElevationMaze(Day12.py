import numpy as np
import sys

###############################################################################
#Dictionary to translate elevations from letters to numbers
############################################################################### 

elevationDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 
                'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 
                'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 
                'p':16, 'q':17, 'r':18, 's':19, 't':20, 
                'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
                'S':1, 'E':26}
            

###############################################################################
#Class used to track the distance from start for each (x,y) coordinate
###############################################################################            

class Node():
    def __init__(self, x, y, elevation, distance):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.distance = distance

###############################################################################
#Function to build a list of nodes from the grid input
###############################################################################  

def buildNodes(grid):
    output = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if(grid[x][y] == 'S'):
                if(startAtEnd):
                    startNode = Node(x, y, grid[x][y], sys.maxsize)
                    output.append(startNode)
                else:
                    startNode = Node(x, y, grid[x][y], 0)
                    output.append(startNode)
            elif(grid[x][y] == 'E'):
                if(startAtEnd):
                    endNode = Node(x, y, grid[x][y], 0)
                    output.append(endNode)
                else:
                    endNode = Node(x, y, grid[x][y], sys.maxsize)
                    output.append(endNode)
            else:
                output.append(Node(x, y, grid[x][y], sys.maxsize))
    return output, startNode, endNode

###############################################################################
#Function to 'visit' one node and change the distances for adjacent nodes
############################################################################### 

def visitNode(unvisitedNodes, visitedNodes, currentNode):
    if(startAtEnd):
        for node in unvisitedNodes:
            if(node.x == currentNode.x and (node.y == currentNode.y + 1 or node.y == currentNode.y - 1) and (elevationDict[node.elevation] >= elevationDict[currentNode.elevation] - 1)):
                if(currentNode.distance + 1 < node.distance):
                    node.distance = currentNode.distance + 1
            elif(node.y == currentNode.y and (node.x == currentNode.x + 1 or node.x == currentNode.x - 1)) and (elevationDict[node.elevation] >= elevationDict[currentNode.elevation] - 1):
                if(currentNode.distance + 1 < node.distance):
                    node.distance = currentNode.distance + 1
    else:
        for node in unvisitedNodes:
            if(node.x == currentNode.x and (node.y == currentNode.y + 1 or node.y == currentNode.y - 1) and (elevationDict[node.elevation] <= elevationDict[currentNode.elevation] + 1)):
                if(currentNode.distance + 1 < node.distance):
                    node.distance = currentNode.distance + 1
            elif(node.y == currentNode.y and (node.x == currentNode.x + 1 or node.x == currentNode.x - 1)) and (elevationDict[node.elevation] <= elevationDict[currentNode.elevation] + 1):
                if(currentNode.distance + 1 < node.distance):
                    node.distance = currentNode.distance + 1
    visitedNodes.append(currentNode)
    unvisitedNodes.remove(currentNode)

###############################################################################
#Function to choose the new current node via smallest distance
############################################################################### 

def newCurrentNode(unvisitedNodes):
    newNode = Node(-1, -1, 'a', sys.maxsize)
    for node in unvisitedNodes:
        if(node.distance < newNode.distance):
            newNode = node
    if(newNode.x == -1):
        print('Fuck')
        unvisitedNodes = []
    return newNode

###############################################################################
#Bool to choose between part 1 and part 2
###############################################################################
startAtEnd = True

if __name__ == '__main__':
    fileObject = open("InputFiles/Day12.txt", "r")
    dataLines = fileObject.read().splitlines()
    gridInv = []
    for line in dataLines:
        gridInv.append(list(line))
    grid = np.array(gridInv).T.tolist()
    unvisitedNodes, startNode, endNode = buildNodes(grid)
    visitedNodes = []

###############################################################################
#Execution for Part 1
###############################################################################
    # while(endNode not in visitedNodes):
    #     currentNode = newCurrentNode(unvisitedNodes)
    #     visitNode(unvisitedNodes, visitedNodes, currentNode)

    # print(currentNode.distance)


###############################################################################
#Execution for Part 2
###############################################################################
    while(unvisitedNodes):
        currentNode = newCurrentNode(unvisitedNodes)
        if(currentNode.x == -1):
            break
        visitNode(unvisitedNodes, visitedNodes, currentNode) 
        print(len(unvisitedNodes))  
    
    closestADist = sys.maxsize
    for node in visitedNodes:
        if(node.elevation == 'a' or node.elevation == 'S'):
            if(node.distance < closestADist):
                print(node.distance)
                closestADist = node.distance

    print(closestADist)

    # print(currentNode.distance)
    # print(currentNode.x)
    # print(currentNode.y)
    # print(currentNode.elevation)
