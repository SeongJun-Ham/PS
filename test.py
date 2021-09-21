dp = [i+1 for i in range(6)]
countList = []
for x in dp:
    for y in dp:
        for z in dp:
            countList.append(x+y+z)

cL = []
for x in range(3,19):
    cL.append([x, countList.count(x)])

print(cL)