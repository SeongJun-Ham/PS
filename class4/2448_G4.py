N = int(input())
cur = 3
tree = ['  *  ', ' * * ', '*****']
atree = ['  *  ', ' * * ', '*****']

while N != cur:
    tree = atree
    atree = []
    for i in tree:
        atree.append(' '*cur + i + ' '*cur)
        
    for i in tree:
        atree.append(i + ' ' + i)
    
    cur *= 2

if cur == 3:
    for t in tree:
        print(t)
else:
    for a in atree:
        print(a)