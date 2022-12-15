class Tree():
    def __init__(self, name):
        self.name = name
        self.files = []
        self.children = []
        self.sumTotal = 0

    def addFile(self, file):
        self.files.append(file)

    def addChild(self, child):
        self.children.append(child)

    def calcTotal(self):
        sum = 0
        for file in self.files:
            sum += int(file.size)
        for child in self.children:
            sum += child.calcTotal()
        self.sumTotal = sum
        return sum

class File():
    def __init__(self, name):
        self.name = name
        self.size = 0

    def setSize(self, fileSize):
        self.size = fileSize

###############################################################################
#Functions used to build the File Tree with the inputs
###############################################################################

def inputFormatting(data):
    output = []
    for line in data:
        output.append(line.split())
    return output

def updateWD(location, currentDirectory):
    if(location == '..'):
        currentDirectory.pop(-1)
    else:
        currentDirectory.append(location)        
        #print(currentDirectory)

def buildTreeList(data):  
    output = [] 
    currentDirectory = []
    for i in range(0, len(data)):
        if(data[i][1] == 'cd'):
            updateWD(data[i][2], currentDirectory)
            if(data[i][2] != '..'):
                output.append(Tree(' '.join(currentDirectory)))   
        elif(data[i][0] != '$' and data[i][0] != 'dir'):
            for j in range(0, len(output)):
                if(output[j].name.split(' ') == currentDirectory):
                    output[j].addFile(File(data[i][1]))
                    output[j].files[-1].setSize(data[i][0])
    return output

def addConnections(trees):
    copy = trees.copy()
    for i in range(0, len(copy)):
        for j in range(0, len(copy)):
            if(copy[i].name.split(' ') == copy[j].name.split(' ')[:-1]):
                trees[i].addChild(trees[j])

###############################################################################
#Functions used to calculate the sum needed for part 1
###############################################################################

def smallTreeSum(trees, n):
    sum = 0
    for tree in trees:
        if(tree.sumTotal <= n):
            sum += tree.sumTotal
    return sum

###############################################################################
#Function used to find the directory for part 2
###############################################################################

def smallestPossibleTree(trees, totalSpace, spaceNeeded):
    freeSpace = totalSpace - trees[0].sumTotal
    deleteSize = spaceNeeded - freeSpace
    smallestTreeSize = trees[0].sumTotal
    for tree in trees:
        if(tree.sumTotal >= deleteSize):
            if(tree.sumTotal < smallestTreeSize):
                smallestTreeSize = tree.sumTotal
    return smallestTreeSize




if __name__ == '__main__':
    fileObject = open("InputFiles/Day7.txt", "r")
    dataLines = fileObject.read().splitlines()
    dataSplit = inputFormatting(dataLines)

    trees = buildTreeList(dataSplit)
    addConnections(trees)
    trees[0].calcTotal()
    print(smallestPossibleTree(trees, 70000000, 30000000))
    
   
    
