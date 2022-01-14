import sys

def rot(dir, arr):
    if dir == 1:
        ahoge = arr.pop()
        arr.insert(0, ahoge)
    elif dir == -1:
        ahoge = arr.pop(0)
        arr.append(ahoge)
    return(arr)

gear = []
for i in range(4):
    gear.append(list(sys.stdin.readline())[:-1])

K = int(sys.stdin.readline())
for i in range(K):
    func = list(map(int, sys.stdin.readline().split()))
    chain = ''
    for j in range(3):
        chain += str(abs(int(gear[j][2]) - int(gear[j + 1][6])))
    if func[0] == 1:
        gear[0] = rot(func[1], gear[0])
        if chain[0] == '1':
            gear[1] = rot(-func[1], gear[1])
            if chain[1] == '1':
                gear[2] = rot(func[1], gear[2])
                if chain[2] == '1':
                    gear[3] = rot(-func[1], gear[3])
    elif func[0] == 2:
        gear[1] = rot(func[1], gear[1])
        if chain[0] == '1':
            gear[0] = rot(-func[1], gear[0])
        if chain[1] == '1':
            gear[2] = rot(-func[1], gear[2])
            if chain[2] == '1':
                gear[3] = rot(func[1], gear[3])
    elif func[0] == 3:
        gear[2] = rot(func[1], gear[2])
        if chain[2] == '1':
            gear[3] = rot(-func[1], gear[3])
        if chain[1] == '1':
            gear[1] = rot(-func[1], gear[1])
            if chain[0] == '1':
                gear[0] = rot(func[1], gear[0])
    elif func[0] == 4:
        gear[3] = rot(func[1], gear[3])
        if chain[2] == '1':
            gear[2] = rot(-func[1], gear[2])
            if chain[1] == '1':
                gear[1] = rot(func[1], gear[1])
                if chain[0] == '1':
                    gear[0] = rot(-func[1], gear[0])

print(eval(gear[0][0] + "*1+" + gear[1][0] + "*2+" + gear[2][0] + "*4+" + gear[3][0] + "*8"))