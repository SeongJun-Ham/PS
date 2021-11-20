import sys

def checkOneLine(OneLineList):
    std = OneLineList[0]
    for i in OneLineList:
        if std != i:
            return False
    return True

def checkEqual(Square):
    for i in Square:
        if checkOneLine(i) == False:
            return False
    std = Square[0][0]
    for i in Square:
        if std != i[0]:
            return False
    return True

def divideNineAreas(inputList):
    N = len(inputList)
    outputList = []
    for i in range(3):
        for j in range(3):
            storage = []
            for k in range(int(N/3)):
                storage.append(inputList[int(N/3)*i+k][int(N/3)*j:int(N/3)*(j+1)])
            outputList.append(storage)
    return outputList

def mainfunc(squareList, count):
    if checkEqual(squareList) == True:
        count[squareList[0][0]] += 1
            
    else:
        againList = divideNineAreas(squareList)
        for i in againList:
            count = mainfunc(i, count)
            
    return count

N = int(sys.stdin.readline())
AllList = []
for i in range(N):
    AllList.append(list(map(int, sys.stdin.readline().split())))

score = mainfunc(AllList, [0, 0, 0])
for i in range(3):
    print(score[i - 1])