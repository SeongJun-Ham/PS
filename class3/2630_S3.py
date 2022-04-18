import sys

def checkOneLine(OneLineList):
    std = OneLineList[0]
    for i in OneLineList:
        if std != i:
            return False
    return True

def checkEqual(Square):
    std = Square[0][0]
    for i in Square:
        for j in i:
            if std != j:
                return [False, std]
    return [True, std]

def divide(inputList):
    N = len(inputList)
    outputList = []
    for i in range(2):
        for j in range(2):
            storage = []
            for k in range(int(N/2)):
                storage.append(inputList[int(N/2)*i+k][int(N/2)*j:int(N/2)*(j+1)])
            outputList.append(storage)
    return outputList

def mainfunc(squareList, count):
    CL = checkEqual(squareList)
    if CL[0] == True:
        count[CL[1]] += 1
            
    else:
        againList = divide(squareList)
        for i in againList:
            count = mainfunc(i, count)
            
    return count

N = int(sys.stdin.readline())
AllList = []
for i in range(N):
    AllList.append(list(map(int, sys.stdin.readline().split())))

score = mainfunc(AllList, [0, 0])
for i in range(2):
    print(score[i])