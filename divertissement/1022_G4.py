def is_num(row, column):
    if row == 0 and column == 0:
        return 1
    elif row < 0 and row + column < 0 and row - column <= 0:
        return ((-row)*2-1)**2 + (-row)*2 + abs(row+column)
    elif column < 0 and row + column <= 0 and column - row < 0:
        return ((-column)*2-1)**2 + (-column)*2*2 + abs(row-column)
    elif row > 0 and row + column > 0 and row - column >= 0:
        return ((row)*2-1)**2 + (row)*2*3 + abs(row+column)
    else:
        return ((column)*2-1)**2 + abs(row-column)

if __name__ == '__main__':
    r1, c1, r2, c2 = map(int, input().split())

    arr = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]

    for r in range(r2 -r1 + 1):
        for c in range(c2 - c1 + 1):
            arr[r][c] = is_num(r1 + r, c1 + c)

    length = max(len(str(arr[0][0])), len(str(arr[0][-1])), len(str(arr[-1][0])), len(str(arr[-1][-1])))

    ans = []

    for r in range(r2-r1+1):
        result = []
        for c in range(c2-c1+1):
            result.append(" "*(length - len(str(arr[r][c]))) + str(arr[r][c]))
            ans.append(result)

    for a in ans:
        print(' '.join(a))