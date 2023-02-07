import sys
sys.setrecursionlimit(100001)

def dfs(edgeVal, bef, cur, index, dis):
    if len(edgeVal[cur]) == index or (len(edgeVal[cur]) == 1 and edgeVal[cur][0][0] == bef):
        global max_distance
        global endEdge
        if max_distance < dis:
            max_distance = dis
            endEdge = cur
        return

    if edgeVal[cur][index][0] != bef:
        dfs(edgeVal, cur, edgeVal[cur][index][0], 0, dis+edgeVal[cur][index][1])

    dfs(edgeVal, bef, cur, index+1, dis)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    edgeValue = [[] for _ in range(N+1)]
    for _ in range(N):
        inp = tuple(map(int, sys.stdin.readline().split()))
        for i in range(1, len(inp)-1, 2):
            edgeValue[inp[0]].append((inp[i], inp[i+1]))

    max_distance = 0
    endEdge = 0
    dfs(edgeValue, 0, 1, 0, 0)
    max_distance = 0
    dfs(edgeValue, 0, endEdge, 0, 0)

    print(max_distance)