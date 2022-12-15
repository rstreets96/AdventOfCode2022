currentDirectory = []

def inputFormatting(data):
    output = []
    for line in data:
        output.append(line.split())
    return output

def updateWD(location):
    if(location == '..'):
        currentDirectory.pop(-1)
    else:
        currentDirectory.append(location)        
        #print(currentDirectory)


def cmdCd(newName, trees):
    if(newName != '..'):
        newTree = Tree(currentDirectory)
        trees = trees[:] + [newTree]
        # i = getParentIndex(trees)
        # trees[i].addChild(trees[-1])
        # trees[-1].addParent(trees[i])
        #print(trees[-1].name)
    return trees

def getParentIndex(trees):
    for i in range(0, len(trees)):
        if(trees[i].name == currentDirectory[:-1]):
            break
    return i

def cmdProcessing(data):  
    output = [] 
    for i in range(0, len(data)):
        if(data[i][1] == 'cd'):
            updateWD(data[i][2])
            if(data[i][2] != '..'):
                output.append(Tree(currentDirectory))
                
    return output

def printTrees(trees):
    for tree in trees:
        print(tree.name)

class Tree():
    def __init__(self, name, files=[], children=[], parent=None):
        self.name = name
        self.parent = parent
        self.files = files
        self.children = children
        self.sumTotal = 0

    def addFile(self, file):
        self.files.append(file)

    def addChild(self, child):
        self.children.append(child)

    def addParent(self, parent):
        self.parent = parent

    def calcTotal(self):
        sum = 0
        for file in self.files:
            sum += file.size
        for child in self.children:
            sum += child.sumTotal
        self.sumTotal = sum

class File():
    def __init__(self, name):
        self.name = name
        self.size = 0

    def setSize(self, fileSize):
        self.size = fileSize



if __name__ == '__main__':
    fileObject = open("InputFiles/Day7.txt", "r")
    dataLines = fileObject.read().splitlines()
    dataSplit = inputFormatting(dataLines)
    trees = cmdProcessing(dataSplit)


    printTrees(trees)
        # for child in tree.children:
        #     print('   %s' %child.name)
        # print('\r')
    