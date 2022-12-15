fullDirectory = {'/':{}}
currentDirectory = []
directoryList = []


def inputFormatting(data):
    output = []
    for line in data:
        output.append(line.split())
    return output



def cmdCd(location):
    if(location == '..'):
        currentDirectory.pop(-1)
    else:
        currentDirectory.append(location)
        directoryList.append(location)
        print(currentDirectory)



def cmdProcessing(data):
    for i in range(0, len(data)):
        if(data[i][1] == 'cd'):
            cmdCd(data[i][2])
        # elif(data[i][1] == 'ls'):
        #     cmdLs(i, data)
   




if __name__ == '__main__':
    fileObject = open("InputFiles/Day7.txt", "r")
    dataLines = fileObject.read().splitlines()
    dataSplit = inputFormatting(dataLines)
    cmdProcessing(dataSplit)
    directoryDict = dict.fromkeys(directoryList)
    print(directoryDict)
    # for line in dataSplit:
    #     print(line)