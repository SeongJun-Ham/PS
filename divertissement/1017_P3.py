def Prime():
    save = [1] * (2001 // 2)
    for i in range(3, int(2001**0.5) + 1, 2):
        if save[i // 2]: save[i // 2 + i::i] = [0] * ((2001 - i - 1) // (2 * i))
    return [2] + [2 * i + 1 for i in range(1, 2001 // 2) if save[i]]


def group_init():
    std = jimin[0]%2
    a = []
    b = []
    for j in jimin:
        if j % 2 == std:
            a.append(j)
        else:
            b.append(j)

    return a, b


def graph_init(a, b):
    graph = [[] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i] + b[j]) in P:
                graph[i].append(b[j])
    
    return graph


def bimatch(n):
    if visited[n]:
        return False
    visited[n] = True

    for num in graph[n]:
        if selected[idxB[num]] == -2:
            pass
        elif selected[idxB[num]] == -1 or bimatch(selected[idxB[num]]):
            selected[idxB[num]] = n
            return True

    return False


def check(s):
    if -1 in s:
        return 0
    else:
        return s.index(-2)


if __name__ == "__main__":
    N = int(input())
    jimin = list(map(int, input().split()))

    P = Prime()
    A_group, B_group = group_init()
    if len(A_group) == len(B_group):
        graph = graph_init(A_group, B_group)
    
        idxA = {}
        idxB = {}
        for m, n in enumerate(B_group):
            idxA[n] = m
        for m, n in enumerate(B_group):
            idxB[n] = m
    
        ans = []
        
        for fix in graph[0]:
            selected = [-1] * (len(B_group))
            selected[idxB[fix]] = -2
            
            for i in range(len(A_group)):
                visited = [False] * len(A_group)
                visited[0] = True
                bimatch(i)
                
            if -1 not in selected:
                ans.append(B_group[selected.index(-2)])
    
        ans.sort()
        if ans:
            print(" ".join(map(str, ans)))
        else:
            print(-1)
    else:
        print(-1)
