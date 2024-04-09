import itertools

def distance(A, B, C):
    result = 0
    for a, b, c in zip(A, B, C):
        if a != b:
            result += 1
        if b != c:
            result += 1
        if c != a:
            result += 1
    return result


if __name__ == "__main__":
    T = int(input())
    while T:
        N = int(input())
        mbti = list(map(str, input().split()))
        if N >= 33:
            ans = 0
        else:
            ans = 12
            mbti.sort()
            comb = itertools.combinations(mbti, 3)
            
            for i in set(comb):
                ans = min(ans, distance(i[0], i[1], i[2]))
        print(ans)
        
        T -= 1
