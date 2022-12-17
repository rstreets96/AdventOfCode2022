def divideByCompartment(rucksacks):
    output = []
    for line in rucksacks:
        compartments = ['','']
        compartments[0], compartments[1] = line[:len(line)//2], line[len(line)//2:]
        output.append(compartments)
    return(output)

def repeatItems(compartments):
    output = []
    for list in compartments:
        overlap = ''
        overlap = set(list[0]).intersection(list[1])
        output.append(overlap)
    return output

def priorityCalc(items):
    priorityLookUp = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 
                    'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 
                    'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 
                    'p':16, 'q':17, 'r':18, 's':19, 't':20, 
                    'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
                    'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 
                    'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 
                    'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 
                    'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 
                    'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}
    totalPriority = 0
    for item in items:
        totalPriority += priorityLookUp[tuple(item)[0]]
    return totalPriority

def groupUp(elves, n):
    output = [elves[i:i+n] for i in range(0, len(elves), n)]
    return output

def findCommonItem(groups):
    output = []
    for group in groups:
        output.append(set(group[0]) & set(group[1]) & set(group[2]))
    return output

if __name__ == '__main__':
    fileObject = open("InputFiles/Day3.txt", "r")
    dataLines = fileObject.read().splitlines()
    compartments = divideByCompartment(dataLines)
    misplacedItems = repeatItems(compartments)
    totalPriority = priorityCalc(misplacedItems)

    groups = groupUp(dataLines, 3)
    badges = findCommonItem(groups)
    badgePriority = priorityCalc(badges)
    print(badgePriority)