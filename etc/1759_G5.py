import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
alpha = list(sys.stdin.readline().split())
vowel = ['a', 'e', 'i','o', 'u']
resultList = []
alpha.sort()

combList = list(combinations(alpha, L))

for i in combList:
    flag = False
    count = 0
    for j in range(L):
        if i[j] in vowel:
            flag = True
        else:
            count += 1
    
    if flag and count >= 2:
        resultList.append(i)

for i in resultList:
    word = ''
    for j in range(L):
        word += i[j]
    print(word)