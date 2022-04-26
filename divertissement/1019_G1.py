N = tuple(map(int, input()))
L = len(N)

def add(all):
    total = [0 for _ in range(10)]
    for i in range(10):
        for j in all:
            try:
                total[i] += j[i]
            except:
                pass
    return total

def multi(n, TL):
    for i in range(10):
        TL[i] *= n
    return TL

total = [int((L-1)*10**(L-2)) for _ in range(10)]
for i in range(L-1):
    total[0] -= 10**i

if L == 1:
    for i in range(N[0] + 1):
        total[i] += 1
    print(" ".join(map(str, total)))
    
elif L == 2:
    first = [0 for _ in range(10)]
    for i in range(N[0]-1):
        first[i+1] += 10**(L-1)
    total = add([total, [(N[0]-1)*10**(L-2) for _ in range(10)], first])
    for i in range(N[1]+1):
        total[i] += 1
        total[N[0]] += 1
    print(" ".join(map(str, total)))
    
else:
    first = [0 for _ in range(10)]
    for i in range(N[0]-1):
        first[i+1] += 10**(L-1)
    first = add([first, [(L-1)*(N[0]-1)*10**(L-2) for _ in range(10)]])
    total = add([total, first])
    for i in range(1, L-1):
        defalt = [0 for i in range(10)]
        for j in range(i):
            defalt[N[j]] += 1
        var = [0 for i in range(10)]
        for j in range(N[i]):
            var[j] += 1
        total = add([total, [N[i]*(L - i - 1)*10**(L - i - 2) for _ in range(10)],multi(N[i]*10**(L - i - 1), defalt), multi(10**(L - i - 1), var)])
    defalt = [0 for i in range(10)]
    for k in range(L-1):
        defalt[N[k]] += 1
    var = [0 for i in range(10)]
    for k in range(N[L-1] + 1):
        var[k] += 1
        
    total = add([total, multi(N[L-1] + 1, defalt), var])
    print(" ".join(map(str, total)))