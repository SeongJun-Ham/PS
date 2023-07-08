import sys


def count_safezone(map):
    result = 0
    for i in map:
        result += i.count(0)
    return result


def viruszone_init(map, seeds):
    global N
    global M
    for i in range(N):
        for j in range(M):
            if map[i][j] == 2:
                map[i][j] = 0
    for seed in seeds:
        map[seed[0]][seed[1]] = 2

        
def search_seed(map):
    result = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 2:
                result.append((i, j))
    return result


def search_safezone_coordinates(map):
    result = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                result.append((i, j))
    return result


def dfs(map):
    N, M = len(map), len(map[0])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    queue = search_seed(map)
    while queue:
        current = queue.pop()
        for i in range(4):
            next = (current[0] + dy[i], current[1] + dx[i])
            if 0 <= next[0] < N and 0 <= next[1] < M:
                if map[next[0]][next[1]] == 0:
                    map[next[0]][next[1]] = 2
                    queue.append((next[0], next[1]))
    return count_safezone(map)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    lab_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    allsafezone = search_safezone_coordinates(lab_map)
    fisrt_seed = search_seed(lab_map)

    ans = 0
    i, j, k = 0, 1, 2
    tmp = []
    flag = True
    while flag:
        walls = [allsafezone[i], allsafezone[j], allsafezone[k]]
        for wall in walls: # 벽 3개 생성
            lab_map[wall[0]][wall[1]] = 1

        ans = max(ans, dfs(lab_map))
        viruszone_init(lab_map, fisrt_seed)

        for wall in walls: # 벽 3개 제거
            lab_map[wall[0]][wall[1]] = 0

        k += 1
        if k == len(allsafezone):
            j += 1
            k = j + 1
            if j == len(allsafezone) - 1:
                i += 1
                j = i + 1
                k = j + 1
                if i == len(allsafezone) - 2:
                    flag = False
    
    print(ans)
