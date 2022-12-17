

def splitPairs(pairs):
    output = []
    for pair in pairs:
        pair = pair.split(',')
        output.append(pair)
    return output

def expandRanges(pairs):
    output = []
    for pair in pairs:
        pair[0] = pair[0].split('-')
        pair[1] = pair[1].split('-')
        output.append(pair)
    return output

def checkFullOverlap(pair):
    fullOverlap = False
    elf1Low = int(pair[0][0])
    elf1High = int(pair[0][1])
    elf2Low = int(pair[1][0])
    elf2High = int(pair[1][1])
    if((elf1Low >= elf2Low) & (elf1High <= elf2High)):
        fullOverlap = True
    elif((elf2Low >= elf1Low) & (elf2High <= elf1High)):
        fullOverlap = True
    return fullOverlap

def checkAnyOverlap(pair):
    overlap = False
    elf1Low = int(pair[0][0])
    elf1High = int(pair[0][1])
    elf2Low = int(pair[1][0])
    elf2High = int(pair[1][1])
    elf1Range = list(range(elf1Low, elf1High + 1))
    elf2Range = list(range(elf2Low, elf2High + 1))
    if(any(check in elf1Range for check in elf2Range)):
        overlap = True
    return overlap

def countFullOverlappedRanges(pairs):
    counter = 0
    for pair in pairs:
        if(checkFullOverlap(pair)):
            counter +=1
    return counter

def countAnyOverlappedRanges(pairs):
    counter = 0
    for pair in pairs:
        if(checkAnyOverlap(pair)):
            counter +=1
    return counter

# def overlapList(pairs):
#     output = []
#     for pair in pairs:
#         if(pair[0][0] != ''):
#             output.append(checkFullOverlap(pair))
#     return output

if __name__ == '__main__':
    fileObject = open("InputFiles/Day4.txt", "r")
    dataLines = fileObject.read().splitlines()
    pairs = splitPairs(dataLines)
    expandedPairs = expandRanges(pairs)
    #fullOverlapCount = countFullOverlappedRanges(expandedPairs)
    anyOverlapCount = countAnyOverlappedRanges(expandedPairs)
    #print(fullOverlapCount)
    print(anyOverlapCount)
