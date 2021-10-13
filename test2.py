import sys

T = int(sys.stdin.readline())
resultList = []

for recursion in range(T):
    func = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arrayStr = str(sys.stdin.readline())
    if func.count("D") > n :
        resultList.append('error')
    else:
        start = 0
        array = []
        for i in range(int(len(arrayStr)/2)-1):
            array.append(arrayStr[2*i+1])
        while len(func)-1:
            current = func.pop(0)
            if current == "R":
                array.reverse()
            elif current == "D":
                array.pop(0)
        resultArray = ','.join(array)
        result = '['
        result += resultArray
        result += ']'
        resultList.append(result)

for i in resultList:
    print(i)
