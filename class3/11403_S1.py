def dfs(node, visited):
    for i, arc in enumerate(arr[node]):
        if arc == 1 and i not in visited:
            visited.append(i)
            tmp = dfs(i, visited)
            for j in range(len(tmp)):
                if tmp[j] == 1:
                    arr[node][j] = 1
    return arr[node]

if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    for n in range(N):
        dfs(n, [n])

    for a in arr:
        print(" ".join(map(str, a)))
