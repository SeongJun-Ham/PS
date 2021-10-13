a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = []
for i in range(1,9):
    if i not in a and i not in b:
        c.append(i)

print(c)
