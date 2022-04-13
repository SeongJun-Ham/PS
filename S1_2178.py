import sys
import copy

N, M = map(int, sys.stdin.readline().split())

maze = ["0"*(M+2)]
for i in range(N):
    maze.append("0" + sys.stdin.readline()[:-1] + "0")
maze.append("0"*(M+2))

queue = [(1, 1)]
visited = [(1,1)]
count = 1

while queue:
        count += 1
        currentQueue = copy.deepcopy(queue)
        queue = []
        for current in currentQueue:
                if (current[0] + 1, current[1]) not in visited and (current[0] + 1, current[1]) not in queue and maze[current[0] + 1][current[1]] == "1":
                        queue.append((current[0] + 1, current[1]))
                        visited.append((current[0] + 1, current[1]))
                if (current[0], current[1] + 1) not in visited and (current[0], current[1] + 1) not in queue and maze[current[0]][current[1] + 1] == "1":
                        queue.append((current[0], current[1] + 1))
                        visited.append((current[0], current[1] + 1))
                if (current[0] - 1, current[1]) not in visited and (current[0] - 1, current[1]) not in queue and maze[current[0] - 1][current[1]] == "1":
                        queue.append((current[0] - 1, current[1]))
                        visited.append((current[0] - 1, current[1]))
                if (current[0], current[1] - 1) not in visited and (current[0], current[1] - 1) not in queue and maze[current[0]][current[1] - 1] == "1":
                        queue.append((current[0], current[1] - 1))
                        visited.append((current[0], current[1] - 1))
        if (N, M) in queue:
                break
        
print(count)
    