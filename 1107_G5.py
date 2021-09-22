import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
ableList = {str(i) for i in range(10)}
if M != 0:
    ableList -= set(map(str, sys.stdin.readline().split()))

neibor100 = abs(N - 100)

def enablenum(num):
    numS = set(str(num))
    for i in numS:
        if i not in ableList:
            return False
    return True

subtract = 0
storage = 1000000

while True:
    if subtract == neibor100:
        break
    if enablenum(N-subtract):
        storage = min(storage, len(str(N-subtract))+subtract)
    if enablenum(N+subtract):
        storage = min(storage, len(str(N+subtract))+subtract)
    subtract += 1

print(min(neibor100, storage))