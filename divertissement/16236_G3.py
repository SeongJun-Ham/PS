import sys
import heapq as h


class Shark:
    def __init__(self):
        self.lev = 2
        self.exp = 0

    def level_sync(self):
        if self.lev == self.exp:
            self.lev += 1
            self.exp = 0


def search_prey(cnt, lev):
    queue = [cnt]
    queue2 = []
    visited = [cnt]
    heap = []
    dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]
    distance = 0

    while not heap and queue:
        distance += 1

        for cnt in queue:
            for i in range(4):
                next = (cnt[0] + dy[i], cnt[1] + dx[i])
                if 0 <= next[0] < N and 0 <= next[1] < N and arr[next[0]][next[1]] <= lev and next not in visited:
                    queue2.append(next)
                    visited.append(next)
                    if 1 <= arr[next[0]][next[1]] < lev:
                        h.heappush(heap, next)

        queue = tuple(queue2)
        queue2 = []

    if heap:
        return True, h.heappop(heap), distance
    else:
        return False, 0, 0


def search_first_position():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return (i, j)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    shark = Shark()
    ans = 0
    flag = True
    pos = search_first_position()
    while flag:
        tmp = search_prey(pos, shark.lev)
        if tmp[0]:
            arr[pos[0]][pos[1]] = 0
            arr[tmp[1][0]][tmp[1][1]] = 9
            ans += tmp[2]
            pos = tmp[1]
            shark.exp += 1
            shark.level_sync()
        else:
            flag = False
    print(ans)
