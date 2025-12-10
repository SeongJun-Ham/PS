import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(cur_v, dis):
    global max_distance
    global longest_vertex
    if dis > max_distance:
        max_distance = dis
        longest_vertex = cur_v
    
    for next_v in edgeValue[cur_v]:
        if visited[next_v[0]]:
            continue
        visited[next_v[0]] = 1
        dfs(next_v[0], dis+next_v[1])
        visited[next_v[0]] = 0


if __name__ == "__main__":
    V = int(input())
    edgeValue = [[] for _ in range(V+1)]
    for _ in range(V):
        temp = tuple(map(int, input().split()))
        for i in range(1, len(temp)-1, 2):
            edgeValue[temp[0]].append((temp[i], temp[i+1]))

    visited = [0]*(V+1)
    max_distance = 0
    longest_vertex = 0

    visited[1] = 1
    dfs(1, 0)

    visited = [0]*(V+1)
    visited[longest_vertex] = 1
    dfs(longest_vertex, 0)

    print(max_distance)
