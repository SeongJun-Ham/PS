def make_prime(n):
    save = [1] * (n // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if save[i // 2]: save[i // 2 + i::i] = [0] * ((n - i - 1) // (2 * i))
    return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]

def divisor_of_square(n):
    result = {}
    i = 0
    while n > 1:
        if i == len(prime):
            result[n] = 2
            break

        if n%prime[i] == 0:
            if prime[i] in result:
                result[prime[i]] += 2
            else:
                result[prime[i]] = 2
            n = n//prime[i]
        else:
            i += 1

    return result

def solution(arr, target):
    if arr == {}:
        return 1

    base = [0]*len(arr)
    keys = list(arr.keys())
    values = list(arr.values())
    result = 0

    while base != values:
        temp = 1
        for i in range(len(base)):
            temp *= keys[i]**base[i]
        
        if temp <= target:
            result += 1

        base[0] += 1
        for i in range(len(base)):
            if base[i] > values[i]:
                base[i] = 0
                base[i+1] += 1

    return result

if __name__ == "__main__":
    prime = make_prime(int(1e+9**(1/2)+1))
    T = int(input())
    ans = []
    for _ in range(T):
        n = int(input())
        k = divisor_of_square(n)
        ans.append(solution(k, n))
    for test_case in range(T):
        print(f"Scenario #{test_case+1}:\n{ans[test_case]}\n")
