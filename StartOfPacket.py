from collections import Counter as ctr

def movingWindow(data, n):
    output = 0
    for i in range(n, len(data)):
        window = data[i-n:i]
        counter = ctr(window)
        output = i
        numUnique = len(counter.keys())
        if(numUnique == n):
            break
    return(output)
        


if __name__ == '__main__':
    fileObject = open("InputFiles/Day6.txt", "r")
    dataLines = fileObject.read()
    window = movingWindow(dataLines, 14)
    print(window)