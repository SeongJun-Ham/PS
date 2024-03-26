import sys

T = int(sys.stdin.readline())

result = []
for _ in range(T):
    K, C = map(int, sys.stdin.readline().split())

    if K%C == 0 or C%K == 0:
            if K == 1:
                if C == 1:
                    result.append(2)
                else:
                    result.append(1)
            elif C == 1:
              if K+1 > 10**9:
                result.append("IMPOSSIBLE")
              else:
                result.append(K+1)
            else:
                result.append("IMPOSSIBLE")
    else:
        m = max(K, C)
        n = min(K, C)
        r = [m, n]
        s = [1, 0]
        t = [0, 1]
        
        while r[1] != 0:
            save = divmod(r[0], r[1])
            r = [r[1], save[1]]
            s = [s[1], s[0]-save[0]*s[1]]
            t = [t[1], t[0]-save[0]*t[1]]
        
        if r[0] == 1:
            if K > C:
                if t[0] < 0:
                    t[0] += K
                if t[0] > 10**9:
                  result.append("IMPOSSIBLE")
                else:
                  result.append(t[0])
            else:
                if s[0] < 0:
                    s[0] += K
                if s[0] > 10**9:
                  result.append("IMPOSSIBLE")
                else:
                  result.append(s[0])
        else:
            result.append("IMPOSSIBLE")
            
for i in result:
    print(i)