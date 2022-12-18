import math

###############################################################################
#Class to track attributes of a monkey
###############################################################################
class Monkey():
    trueMonkey = None
    falseMonkey = None
    inspectCount = 0
    lcm = 0

    def __init__(self, name = None):
        self.items = []
        self.name = name

    def addItem(self, item):
        self.items.append(item)

    def addOperation(self, operation):
        self.operation = operation
        
    def setDivider(self, divider):
        self.divider = int(divider)
        
    def setRecipients(self, trueMonkeyIndex, falseMonkeyIndex):
        self.trueMonkeyIndex = int(trueMonkeyIndex)
        self.falseMonkeyIndex = int(falseMonkeyIndex)

    def runOperation(self, item):
        old = item
        item = math.floor(eval(self.operation) / 3)
        return item

    def runOperationWithoutRelief(self, item):
        old = item
        item = math.floor(eval(self.operation))
        return item 
    
    def test(self, item):
        return (item % self.divider == 0)


###############################################################################
#Functions to complete Part 1
###############################################################################        

def buildMonkeyList(data):
    output = []
    trueIndex = 0
    falseIndex = 0
    for line in data:
        if(line):
            if(line[0] == 'Monkey'):
                output.append(Monkey(line[1][:-1]))
            elif(line[0] == 'Starting'):
                for item in line[2:]:
                    if ',' in item:
                        output[-1].addItem(item[:-1])
                    else:
                        output[-1].addItem(item)
            elif(line[0] == 'Operation:'):
                output[-1].operation = ' '.join(line[3:])
            elif(line[0] == 'Test:'):
                output[-1].setDivider(line[-1])
            elif(line[1] == 'true:'):
                trueIndex = line[-1]
            elif(line[1] == 'false:'):
                falseIndex = line[-1]
        output[-1].setRecipients(trueIndex, falseIndex)   
    leastCommonMultipleOfDividers(output)
    return(output)

def oneRound(monkeys):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspectCount += 1
            if(relief):
                item = monkey.runOperation(int(item))
            else:
                item = monkey.runOperationWithoutRelief(int(item))
            if(item >= monkey.lcm):
                item = item % monkey.lcm
            if(monkey.test(int(item))):
                monkeys[monkey.trueMonkeyIndex].items.append(item)
            else:
                monkeys[monkey.falseMonkeyIndex].items.append(item)
        monkey.items = []

###############################################################################
#Functions to complete Part 2
###############################################################################  

def leastCommonMultipleOfDividers(monkeys):
    dividers = []
    for monkey in monkeys:
        dividers.append(monkey.divider)
    lcm = math.lcm(*dividers)
    for monkey in monkeys:
        monkey.lcm = lcm


###############################################################################
#Boolean and round count to choose betwen Part 1 and Part 2
###############################################################################

relief = False
roundCount = 10000

if __name__ == '__main__':
    fileObject = open("InputFiles/Day11.txt", "r")
    dataLines = fileObject.read().splitlines()
    splitLines = []
    for line in dataLines:
        splitLines.append(line.split())
        
    monkeys = buildMonkeyList(splitLines)

    #print(leastCommonMultipleOfDividers(monkeys)

    for i in range(roundCount):
        oneRound(monkeys)

    for monkey in monkeys:
        print('{} {}'.format(monkey.items, monkey.inspectCount))



   
