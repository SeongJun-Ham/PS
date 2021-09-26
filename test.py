import sys

T = int(sys.stdin.readline())

for recursion in range(T):
    func = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arrayStr = str(sys.stdin.readline())
    if func.count("D") > n :
        print('error')
    else:
        flag = 1
        array = list(map(str, arrayStr[1:-2].split(",")))
        for fun in func:
            if fun == "R" and flag == 1:
                flag = 0
            elif fun == "R" and flag ==0:
                flag = 1
            elif fun == "D":
                if flag == 1:
                    array.pop(0)
                elif flag == 0:
                    array.pop()
        if flag == 0:
            array.reverse()
        resultArray = ','.join(array)
        result = '['
        result += resultArray
        result += ']'
        print(result)