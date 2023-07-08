def OneOfNum(N):
    save = 0
    ans = 0
    storage = list(bin(N)[2:])
    L = len(storage)
    for i in range(L-1):
        if storage[i] == "1":
            ans += (L-i-1)*(2**(L-i-2))+save*(2**(L-i-1))
            save += 1
    if storage[L-1] == "1":
        ans += save*2 + 1
    else:
        ans += save
    return ans


A, B = map(int, input().split())

print(OneOfNum(B) - OneOfNum(A-1))
