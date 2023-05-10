import sys


def ComponentSum(SliceOfPizzaSize):
    global OrderedSize
    tmp = []
    for start in range(-len(SliceOfPizzaSize), 0):
        token = 0
        for end in range(start, start + len(SliceOfPizzaSize) - 1):
            token += SliceOfPizzaSize[end]
            if token <= OrderedSize:
                tmp.append(token)
                
    token += SliceOfPizzaSize[end + 1]
    if token <= OrderedSize:
        tmp.append(token)
    return tmp


if __name__ == "__main__":
    OrderedSize = int(sys.stdin.readline())
    m, n = map(int, sys.stdin.readline().split())

    M = []
    N = []

    for _ in range(m):
        M.append(int(input()))
    for _ in range(n):
        N.append(int(input()))

    MComponentSum = ComponentSum(M)
    NComponentSum = ComponentSum(N)
    MComponentSum.sort()
    NComponentSum.sort()

    ans = 0
    for i in range(-1, -len(MComponentSum) - 1, -1): # M만으로 만듦
        if MComponentSum[i] == OrderedSize:
            ans += 1
        elif MComponentSum[i] < OrderedSize:
            break
    for i in range(-1, -len(NComponentSum) - 1, -1): # N만으로 만듦
        if NComponentSum[i] == OrderedSize:
            ans += 1
        elif NComponentSum[i] < OrderedSize:
            break
    
    i, j = 0, -1
    while i < len(MComponentSum) and j >= -len(NComponentSum):
        Sum = MComponentSum[i] + NComponentSum[j]
        if Sum > OrderedSize:
            j -= 1
        elif Sum < OrderedSize:
            i += 1
        else:
            ntoken = 1
            mtoken = 1
            while i < len(MComponentSum)-1 and MComponentSum[i] == MComponentSum[i+1]:
                i += 1
                ntoken += 1
            while j > -len(NComponentSum) and NComponentSum[j] == NComponentSum[j-1]:
                j -= 1
                mtoken += 1
            i += 1
            j -= 1
            ans += ntoken*mtoken

    print(ans)
