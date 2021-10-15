import sys

N, M = map(int, sys.stdin.readline().split())
illustratedBook = {}
illustratedBookR = {}
result = ''

for i in range(N):
    func = sys.stdin.readline()[:-1]
    illustratedBook[str(i+1)] = func
    illustratedBookR[func] = str(i+1)

for i in range(M):
    func = sys.stdin.readline()[:-1]

    try:
        result += illustratedBook[func]+'\n'
    except:
        result += illustratedBookR[func]+'\n'

print(result[:-1])