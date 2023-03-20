letter = list(input())
bomb = list(input())
key = bomb[0]
stack = []

while letter:
    tok = letter.pop()
    stack.append(tok)

    if tok == key:
        if stack:
            flag = True
            try:
                for t in range(len(bomb)):
                    if bomb[t] != stack[-t-1]:
                        flag = False
                        break
            except:
                flag = False

            if flag:
                for _ in range(len(bomb)):
                    stack.pop()
                    
if stack:
    ans = "".join(list(reversed(stack)))
    print(ans)
else:
    print("FRULA")