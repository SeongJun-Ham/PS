import sys

def checkOneLine(OneLine):
    std = OneLine[0]
    for i in OneLine:
        if std != i:
            return False
    return True

def isEqual(Square):
    for i in Square:
        if checkOneLine(i) == False:
            return False
    std = Square[0][0]
    for i in Square:
        if std != i[0]:
            return False
    return True

def divideFourAreas(inputList):
    N = len(inputList)
    outputList = []
    for i in range(2):
        for j in range(2):
            storage = []
            for k in range(int(N/2)):
                storage.append(inputList[int(N/2)*i+k][int(N/2)*j:int(N/2)*(j+1)])
            outputList.append(storage)
    return outputList

def mainfunc(squareList, Sentence):
    if isEqual(squareList):
        Sentence += squareList[0][0]
    
    else:
        storage = ""
        againList = divideFourAreas(squareList)
        for i in againList:
            storage += mainfunc(i, Sentence)
        Sentence += "({})".format(storage)
        
    return Sentence

N = int(sys.stdin.readline())
AllList = []
result = ""

for i in range(N):
    AllList.append(list(sys.stdin.readline()[:-1]))

print(mainfunc(AllList, result))