N = int(input())
prime = []
for i in range(2, N + 1):
    flag = True
    for j in prime:
        if j > int(i**(1/2)):
            break
        if i % j == 0:
            flag = False
            break
    if flag:
        prime.append(i)

count = 0
flag = True
while flag:
    result = 0
    flag = False
    for i in range(1, len(prime) + 1):
        result += prime[-i]
        if result == N:
            flag = True
            count += 1
            prime.pop()
            break
        if result > N:
            flag = True
            prime.pop()
            break

print(count)