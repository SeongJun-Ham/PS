D, P, Q = map(int, input().split())

result = (((D//max(P, Q))+1)*max(P, Q))

if result == D:
    print(result)
else:
    for i in range(D//max(P, Q) + 1):
        T = D - i * max(P, Q)
        if T%min(P, Q) == 0:
            result = min(result, i*max(P, Q) + min(P, Q)*((T//min(P, Q))))
            break
        else:
            result = min(result, i*max(P, Q) + min(P, Q)*((T//min(P, Q)+1)))
    print(result)