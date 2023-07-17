import heapq as h
import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    if N == 1:
        a = int(sys.stdin.readline())
        print(a)
    elif N == 2:
        a = int(sys.stdin.readline())
        b = int(sys.stdin.readline())
        print(a)
        print(min(a, b))
    else:
        a = int(sys.stdin.readline())
        b = int(sys.stdin.readline())
        h_f = [max(-a, -b)]
        h_b = [max(a, b)]
        toggle = 0
        print(a)
        print(min(a, b))
    
        for _ in range(N-2):
            num = int(sys.stdin.readline())
            if toggle == 0:
                if h_b[0] < num:
                    h.heappush(h_f, -h.heappop(h_b))
                    h.heappush(h_b, num)
                else:
                    h.heappush(h_f, -num)
            else:
                if -h_f[0] > num:
                    h.heappush(h_b, -h.heappop(h_f))
                    h.heappush(h_f, -num)
                else:
                    h.heappush(h_b, num)
    
            toggle = (toggle + 1)%2
            print(-h_f[0])
