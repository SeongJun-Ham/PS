import sys
input = sys.stdin.readline

def D(num):
    return (2*num)%10000


def S(num):
    return (num-1)%10000


def L(num):
    a, b = divmod(10*num, 10000)
    return a+b


def R(num):
    a, b = divmod(num, 10)
    return 1000*b+a


def dp(s, e):
    stack = [(s, '')]
    check = [1]*10000
    check[s] = 0
    flag = True
    while stack and flag:
        tmp = []
        for _ in range(len(stack)):
            current = stack.pop()
            if check[D(current[0])]:
                if D(current[0]) == e:
                    ans = current[1]+'D'
                    flag = False
                    break
                check[D(current[0])] = 0
                tmp.append((D(current[0]), current[1]+'D'))
            if check[S(current[0])]:
                if S(current[0]) == e:
                    ans = current[1]+'S'
                    flag = False
                    break
                check[S(current[0])] = 0
                tmp.append((S(current[0]), current[1]+'S'))
            if check[L(current[0])]:
                if L(current[0]) == e:
                    ans = current[1]+'L'
                    flag = False
                    break
                check[L(current[0])] = 0
                tmp.append((L(current[0]), current[1]+'L'))
            if check[R(current[0])]:
                if R(current[0]) == e:
                    ans = current[1]+'R'
                    flag = False
                    break
                check[R(current[0])] = 0
                tmp.append((R(current[0]), current[1]+'R'))
        stack = tmp
    return ans


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(dp(A, B))
