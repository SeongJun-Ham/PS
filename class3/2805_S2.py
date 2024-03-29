import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    height = list(map(int, input().split()))
    height.sort(reverse=True)
    tree = [0]
    
    idx = len(height)-1
    for i in range(1, len(height)):
        token = tree[-1]+i*(height[i-1]-height[i])
        if token >= M:
            idx = i - 1
            break
        tree.append(token)
    
    ans = int(height[idx] - (M - tree[-1])/(idx+1))
    
    print(ans)
