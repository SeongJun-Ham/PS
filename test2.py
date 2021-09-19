vertexList = [1, 2, 3, 4, 5]
edgeList = [[1, 3], [1, 4],[4, 5], [4, 3], [3, 2], [3, 1], [4, 1], [5, 4], [3, 4], [2, 3]]

for x in range(7):
    if x in vertexList:
        print('True')
    else:
        print('False')