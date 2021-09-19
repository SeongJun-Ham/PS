a = int(input())
b = list(map(int, input().split()))
print(100*sum(b)/(a*max(b)))