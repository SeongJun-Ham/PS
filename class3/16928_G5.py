import sys
input = sys.stdin.readline

def bfs():
    global ladder
    global snake
    check = [0]*101
    check[1] = 1

    result = 0
    while check[100] == 0:
        tmp = [0]*101
        for i in range(1, 101):
            if check[i]:
                for j in range(1, 7):
                    if i+j <= 100:
                        if i+j in ladder:
                            tmp[ladder[i+j]] += 1
                        elif i+j in snake:
                            tmp[snake[i+j]] += 1
                        else:
                            tmp[i+j] += 1
        check = tmp
        result += 1
    return result

if __name__ == "__main__":
    N, M = map(int, input().split())
    ladder = {}
    snake = {}
    
    #ladder input
    for _ in range(N):
        start, end = map(int, input().split())
        ladder[start] = end
    #snake input
    for _ in range(M):
        start, end = map(int, input().split())
        snake[start] = end

    ans = bfs()
    print(ans)
