def linesToInputs(data):
    for line in data:
       line = line.split(' ')
    return data


fileObject = open("InputFiles/Day2.txt", "r")
dataLines = fileObject.read().splitlines()
inputs = linesToInputs(dataLines)
print(inputs)