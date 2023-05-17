import sys


def starFlagPainting(mineArray, idx):
    for i in range(-1, 2, 1):
        if mineArray[1][idx + i] == '#':
            mineArray[1] = mineArray[1][:idx + i] + '*' + mineArray[1][idx + i + 1:]
    return mineArray


def XFlagPainting(mineArray, idx):
    for i in range(-1, 2, 1):
        if mineArray[1][idx + i] == '#':
            mineArray[1] = mineArray[1][:idx + i] + 'X' + mineArray[1][idx + i + 1:]
    return mineArray


def checkMine(token, count):
    for t in token:
        if t == '*':
            count[0] += 1
        elif t == 'X':
            count[1] += 1
        else:
            count[2] += 1
    return count


def searchMine(length, mineArray, flag):
    i = 1
    while True:
        count = [0, 0, 0] # 인덱스 순으로 지뢰 있음, 지뢰 없음, 알 수 없음
        count = checkMine(mineArray[1][i - 1:i + 2], count)

        if str(count[0]) == mineArray[0][i] and count[2] != 0:
            mineArray = XFlagPainting(mineArray, i)
            flag = True
        elif str(count[0] + count[2]) == mineArray[0][i] and count[2] != 0:
            mineArray = starFlagPainting(mineArray, i)
            flag = True
        i += 1

        if i == length + 1 and flag == True:
            i = 1
            flag = False
        elif i == length + 1 and flag == False:
            break
    return mineArray
            
def searchMine2(length, mineArray, idx):
    if idx == length + 1:
        return

    global result
    if mineArray[1][idx] == '#':
        mineArray[1] = mineArray[1][:idx] + '*' + mineArray[1][idx + 1:]
        tmp = searchMine(length, mineArray, True)
        result = max(result, tmp[1].count('*'))
        mineArray[1] = mineArray[1][:idx] + '#' + mineArray[1][idx + 1:]
    searchMine2(length, mineArray, idx + 1)


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    ans = []
    for t in range(T):
        N = int(sys.stdin.readline())
        mine =['X' + sys.stdin.readline().rstrip() + 'X' for _ in range(2)]
        mine = searchMine(N, mine, False)
        result = mine[1].count('*')
        searchMine2(N, mine, 1)
        ans.append(result)


    for i in range(T):
        print(ans[i])
