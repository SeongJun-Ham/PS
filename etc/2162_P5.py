import sys

input = sys.stdin.readline

def mul(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]


def ccw(p1, p2, p3):
    v1 = (p2[0]-p1[0], p2[1] - p1[1])
    v2 = (p3[0]-p1[0], p3[1] - p1[1])
    res = mul(v1, v2)

    if res < 0:
        return 1
    elif res > 0:
        return -1
    else:
        return 0


def is_same_group(l1, l2):
    p1 = (l1[0], l1[1])
    p2 = (l1[2], l1[3])
    p3 = (l2[0], l2[1])
    p4 = (l2[2], l2[3])

    res = [0, 0, 0, 0]
    res[0] = ccw(p1, p2, p3)
    res[1] = ccw(p1, p2, p4)
    res[2] = ccw(p3, p4, p1)
    res[3] = ccw(p3, p4, p2)
    if res == [0, 0, 0, 0]:
        if (p1[0]-p3[0])*(p1[0]-p4[0]) <= 0 and (p1[1]-p3[1])*(p1[1]-p4[1]) <= 0:
            return True
        elif (p2[0]-p3[0])*(p2[0]-p4[0]) <= 0 and (p2[1]-p3[1])*(p2[1]-p4[1]) <= 0:
            return True
        elif (p3[0]-p1[0])*(p3[0]-p2[0]) <= 0 and (p3[1]-p1[1])*(p3[1]-p2[1]) <= 0:
            return True
        elif (p4[0]-p1[0])*(p4[0]-p2[0]) <= 0 and (p4[1]-p1[1])*(p4[1]-p2[1]) <= 0:
            return True
        else:
            return False
    else:
        if res[0]*res[1] <= 0 and res[2]*res[3] <= 0:
            return True
        else:
            return False


def find(x):
    global parent
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union():
    global parent
    for i in range(len(parent)):
        find(i)


if __name__ == "__main__":
    N = int(input())
    line = [tuple(map(int, input().split())) for _ in range(N)]

    parent = list(range(N))
    i, j = 0, 1
    while i != N-1:
        if is_same_group(line[i], line[j]):
            parent[find(i)] = min(find(i), find(j))
            parent[find(j)] = min(find(i), find(j))
        j += 1
        if j == N:
            i += 1
            j = i + 1

    union()

    res1 = list(set(parent))
    res2 = 0
    for i in range(len(res1)):
        res2 = max(res2, parent.count(res1[i]))

    print(len(res1))
    print(res2)