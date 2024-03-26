import sys


def strlenW(W, K):
    tmp = [[] for _ in range(26)]
    minresult = len(W)
    maxresult = 0
    for i, token in enumerate(W):
        tmp[ord(token)-97].append(i)
        if len(tmp[ord(token)-97]) >= K:
            minresult = min(minresult, tmp[ord(token)-97][-1] - tmp[ord(token)-97][-K] + 1)
            maxresult = max(maxresult, tmp[ord(token)-97][-1] - tmp[ord(token)-97][-K] + 1)

    if maxresult != 0:
        return "{} {}".format(minresult, maxresult)
    else:
        return -1


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        W = sys.stdin.readline().rstrip()
        K = int(sys.stdin.readline())
        print(strlenW(W, K))
