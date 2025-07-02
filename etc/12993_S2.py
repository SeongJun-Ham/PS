a, b = map(int, input().split())

ans = 1
while a+b != 0:
    if a%3 + b%3 == 1:
        a //= 3
        b //= 3
    else:
        ans = 0
        break
print(ans)