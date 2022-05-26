import sys
arl = [sys.stdin.readline().rstrip() for _ in range(9)]
arr = [[0]*9 for i in range(9)]

for i in range(9):
    for j in range(9):
        arr[i][j] = int(arl[i][j])
    
def check(x, y, num, arr):
    if num in arr[x]:
        return False
    if num in [i[y] for i in arr]:
        return False
    for i in range(3):
        if num in arr[3*(x//3)+i][3*(y//3):3*(y//3)+3]:
            return False
    return True

def searchNext(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return (i, j)
    return (-1, -1)

queue = []

if searchNext(arr) != (-1, -1):
    x, y = searchNext(arr)[0], searchNext(arr)[1]
    for n in range(9,0,-1):
        if check(x, y, n, arr):
            queue.append((x, y, n, 1))
    arr[queue[-1][0]][queue[-1][1]] = queue[-1][2]

    while queue:
        if searchNext(arr) != (-1, -1):
            cur = queue[-1]
            x, y = searchNext(arr)[0], searchNext(arr)[1]
            for n in range(9, 0, -1):
                if check(x, y, n, arr):
                    queue.append((x, y, n, cur[3] + 1))
            
            if cur == queue[-1]:
                current = queue.pop()
                arr[current[0]][current[1]] = 0
                while queue and current[3] - 1 == queue[-1][3]:
                    current = queue.pop()
                    arr[current[0]][current[1]] = 0
                    
            arr[queue[-1][0]][queue[-1][1]] = queue[-1][2]
        else:
            break
    
    for i in range(9):
        print("".join(map(str, arr[i])))
        
else:
    for i in range(9):
        print("".join(map(str, arr[i])))