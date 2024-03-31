import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    seq = input().rstrip()
    check = []

    for i in range(1, M-1):
        if seq[i] == 'O' and seq[i-1] == 'I' and seq[i+1] == 'I':
            check.append(i)

    ans = 0
    for i in range(len(check)):
        if i+N-1 < len(check) and check[i+N-1] == check[i]+2*(N-1):
            ans += 1

    print(ans)
