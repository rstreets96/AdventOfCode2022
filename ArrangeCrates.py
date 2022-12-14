def parsingInput(data):
    output = []
    for line in data:        
        if(line == ' 1   2   3   4   5   6   7   8   9 '):
            break
        line = [line[i:i+3] for i in range(0, len(line), 4)]
        output.append(line)
    return output




if __name__ == '__main__':
    fileObject = open("InputFiles/Day5.txt", "r")
    dataLines = fileObject.read().splitlines()
    parsedData = parsingInput(dataLines)
    #crateColumns = originalState(parsedData)
    for line in parsedData:
        print(line)