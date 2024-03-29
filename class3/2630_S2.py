import sys
input = sys.stdin.readline

def cut(paper):
    token = check(paper[0][0], paper)
    if token == 0:
        global w_paper
        w_paper +=1
        return
    elif token == 1:
        global b_paper
        b_paper += 1
        return
    
    L = len(paper)//2
    for i in range(2):
        for j in range(2):
            tmp = []
            for l in range(L):
                tmp.append(paper[i*L+l][j*L:(j+1)*L])
            cut(tmp)


def check(key, anyList):
    flag = True
    for a in anyList:
        if a.count(key) != len(a):
            flag = False
            break
    
    if flag:
        return key
    else:
        return -1

if __name__ == "__main__":
    N = int(input())
    paper_list = []
    for _ in range(N):
        paper_list.append(list(map(int, input().split())))

    w_paper = 0
    b_paper = 0
    cut(paper_list)
    
    print(w_paper)
    print(b_paper)
