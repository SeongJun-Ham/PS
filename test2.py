<<<<<<< HEAD
k = '3 3\nemtpy\n4 6\n'
print(k)
print("------------------")
print(k[:-1])
=======
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
>>>>>>> 33a313da99d20e810397c0a98f3f04828ca3fd6e
