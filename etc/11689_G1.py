def Prime(n):
    if n < 2: return []
    n += 1
    save = [1] * (n // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if save[i // 2]: save[i // 2 + i::i] = [0] * ((n - i - 1) // (2 * i))
    return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]


if __name__ == "__main__":
    N = int(input())
    ans = N
    if N == 1:
        print(1)
    else:
        p_num = Prime(int(N**0.5))
        for p in p_num:
            if N % p == 0:
                while N % p == 0:
                    N = N // p
                ans = int(ans // p) * (p - 1)

        if N != 1:
            ans = ans * (N - 1) // N

        print(ans)
