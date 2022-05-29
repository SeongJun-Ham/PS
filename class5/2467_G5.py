import sys

N = int(sys.stdin.readline())
solution = tuple(map(int, sys.stdin.readline().split()))
i, j = 0, 1
ans = (2*10**9, 0, -1)

while i + j != N-1:
    result = solution[i] + solution[-j]
    ans = min(ans, (abs(result), i, -j))
        
    if result > 0:
        j += 1
    elif result < 0:
        i += 1
    else:
        ans = (abs(result), i, -j)
        break
    
if ans[0] != abs(solution[i] + solution[-j]):
        ans = min(ans, (abs(solution[i] + solution[-j]), i, -j))

print("%d %d" % (solution[ans[1]], solution[ans[2]]))