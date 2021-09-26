import sys

T = int(sys.stdin.readline())

for recursion in range(T):
    func = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arrayStr = str(sys.stdin.readline())
    RStack = 1
    DLeft = 0
    DRight = 0
    
    if func.count("D") > n :
        print('error')
    else:
        array = list(map(str, arrayStr[1:-2].split(",")))
        for fun in func:
            if fun == "R":
                RStack += 1
            elif fun == "D":
                if RStack % 2:
                    DLeft += 1
                else:
                    DRight += 1
        array = array[DLeft:n-DRight]
        if not RStack % 2:
            array.reverse()
        resultArray = ','.join(array)
        result = '['
        result += resultArray
        result += ']'
        print(result)