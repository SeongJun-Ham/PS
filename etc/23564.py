T = input().strip()

ans1 = ""
ans2 = []
while T:
    token = [T[0], [1], 1]
    i = 0
    j = 1
    while True:
        if i + j >= len(T):
            break
        elif T[i] != T[i + j]:
            token = [T[i + j], i + j, 1]
            i += j
            j = i + 1
        else:
            i += j
            token[2] += 1
    ans1 += token[0]
    ans2.append(token[2])
    if token[2] == len(T):
        break
    T = T[:token[1]]

print(ans1[::-1])
ans2 = reversed(ans2)
print(" ".join(map(str, ans2)))
