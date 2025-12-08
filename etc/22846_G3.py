def Prime(n):
    if n < 2: return []
    n += 1
    save = [1] * (n // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if save[i // 2]: save[i // 2 + i::i] = [0] * ((n - i - 1) // (2 * i))
    return [1, 2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]

if __name__ == "__main__":
    N = int(input())
    p_num = Prime(N)

    dp = [0 for _ in range(N+1)]
    for i in range(N-1, 0, -1):
        for p in p_num:
            if i+p > N:
                break
            if i%p == 0 and dp[i+p] == 0:
                dp[i] = 1
                break
    if dp[1]:
        print("Kali")
    else:
        print("Ringo")