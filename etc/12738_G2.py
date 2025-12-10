import sys
from bisect import bisect_left
input = sys.stdin.readline

def LIS(seq):
    result = [-sys.maxsize]
    for term in seq:
        if term > result[-1]:
            result.append(term)
        else:
            result[bisect_left(result, term)] = term
    return len(result)-1


if __name__ == "__main__":
    N = int(input())
    sequence = tuple(map(int, input().split()))
    print(LIS(sequence))
