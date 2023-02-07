def dfs(index1, index2):
    if index1 == N:
        global count
        count += 1
        return

    if index2 == N:
        return

    if check[0][index2] == 0 and check[1][index1-index2] == 0 and check[2][index1+index2] == 0:
        check[0][index2] = 1
        check[1][index1-index2] = 1
        check[2][index1+index2] = 1
        dfs(index1+1, 0)
        check[0][index2] = 0
        check[1][index1-index2] = 0
        check[2][index1+index2] = 0

    dfs(index1, index2+1)

if __name__ =="__main__":
    N = int(input())
    check = [[0]*N, [0]*(2*N-1), [0]*(2*N-1)]
    count = 0
    dfs(0, 0)
    print(count)