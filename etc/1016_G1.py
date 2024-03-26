def pPrime(n):
    if n < 2: return []
    n += 1
    save = [1] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if save[i // 2]: save[i * i // 2::i] = [0] * ((n - i * i - 1) // (2 * i) + 1)
    return [4] + [(2 * i + 1)**2 for i in range(1, n // 2) if save[i]]

S, E = map(int, input().split())

Sieve = [1 for i in range(E - S + 1)]

powPrime = pPrime(int(E**0.5))

for p in powPrime:
    if p < S:
        Sieve[(p - S%p)%p :: p] = [0] * (E//p - (S-1)//p)
    elif p > S:
        Sieve[p-S :: p] = [0] * (E//p - (S-1)//p)
    else:
        Sieve[0 :: p] = [0] * (E//p)
print(sum(Sieve))