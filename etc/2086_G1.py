a, b = map(int, input().split())

a %= 1500000000
b %= 1500000000

storage = {0 : 0, 1 : 1, 2 : 1}

if a < 2:
    sa = storage[a]

i = 3

while i != b+3:
    storage[i%3] = (storage[(i+1)%3] + storage[(i+2)%3])%(2*(10**9))
    if i == a+1:
        sa = storage[i%3]
    
    i += 1

print(storage[(b+2)%3]-sa)