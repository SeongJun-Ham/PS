import sys

M = int(sys.stdin.readline())
S = [0 for x in range(21)]

for x in range(M):
    func = sys.stdin.readline()[:-1]
    if func == "all":
        S = [1 for i in range(21)]
    elif func == "empty":
        S = [0 for i in range(21)]
    else:
        func, x = func.split()
        x = int(x)
        if func == "add":
            S[x] = 1
        elif func == "remove":
            S[x] = 0
        elif func == "check":
            print(S[x])
        elif func == "toggle":
            if S[x] == 1:
                S[x] = 0
            else:
                S[x] = 1