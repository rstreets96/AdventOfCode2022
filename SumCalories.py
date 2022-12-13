def splitByElf(data):
    parsedData = [[]]
    for item in data:
        if item == '':
            parsedData.append([])
        else:
            parsedData[-1].append(item)
    return parsedData

def sumEachElf(data):
    elfSums = []
    for elf in data:
        sum = 0
        for calories in elf:
            sum += int(calories)
        elfSums.append(sum)
    return(elfSums)

def findGreatest(data):
    greatest = 0
    for elf in data:
        if(elf > greatest):
            greatest = elf
    return greatest

def findGreatestThree(data):
        data.sort(reverse = True)
        return data[:3]

def simpleSum(data):
    sum = 0
    for item in data:
        sum += int(item)
    return sum

if __name__ == '__main__':
    fileObject = open("InputFiles/Day1.txt", "r")
    dataLines = fileObject.read().splitlines()
    dataPerElf = splitByElf(dataLines)
    elfSums = sumEachElf(dataPerElf)
    greatestElf = findGreatest(elfSums)
    greatestThreeElves = findGreatestThree(elfSums)
    topThreeElfSum = simpleSum(greatestThreeElves)
    print(topThreeElfSum)