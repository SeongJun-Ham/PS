import sys

def slope1(a, b):
    return round(((b[1] - a[1])/(b[0] - a[0])), 10)

def slope2(a, b):
    return round(((b[0] - a[0])/(b[1] - a[1])), 10)

T = int(sys.stdin.readline())
for _ in range(T):
    cdn = tuple(map(int, sys.stdin.readline().split()))
    p1 = min((cdn[0], cdn[1]), (cdn[2], cdn[3]))
    p2 = max((cdn[0], cdn[1]), (cdn[2], cdn[3]))
    s1 = min((cdn[4], cdn[5]), (cdn[6], cdn[7]))
    s2 = max((cdn[4], cdn[5]), (cdn[6], cdn[7]))
    if s1 == p1 or s1 == p2 or s2 == p1 or s2 == p2:
        print("T")
    elif s1 == s2 and p1 == p2:
        if s1 == p1:
            print("T")
        else:
            print("F")
    elif s1 == s2:
        # 사각형이 점
        y = slope1(p1, p2)*(s1[0] - p1[0]) + p1[1]
        if y == s1[1]:
            print("T")
        else:
            print("F")
    elif s1[0] == s2[0]:
        # 사각형이 세로
        if p1 == p2:
            if p1[0] == s1[0] and min(s1[1], s2[1]) <= p1[0] <= max(s1[1], s2[1]):
                print("T")
            else:
                print("F")
        elif p1[0] == p2[0]:
            if p1[0] != s1[0]:
                print("F")
            elif min(p1[1], p2[1]) > max(s1[1], s2[1]) or max(p1[1], p2[1]) < min(s1[1], s2[1]):
                print("F")
            else:
                print("T")
        elif p1[1] == p2[1]:
            if min(p1[0], p2[0]) <= s1[0] <= max(p1[0], p2[0]) and min(s1[1], s2[1]) <= p1[1] <= max(s1[1], s2[1]):
                print("T")
            else:
                print("F")
        elif p1[0] <= s1[0] <= p2[0]:
            y = slope1(p1, p2)*(s1[0]-p1[0]) + p1[1]
            if min(s1[1], s2[1]) <= y <= max(s1[1], s2[1]):
                print("T")
            else:
                print("F")
        else:
            print("F")
    elif s1[1] == s2[1]:
        # 사각형이 가로
        if p1 == p2:
            if s1[1] == p1[1] and s1[0] <= p1[0] <= s2[0]:
                print("T")
            else:
                print("F")
        elif p1[0] == p2[0]:
            if min(p1[1], p2[1]) <= s1[1] <= max(p1[1], p2[1]) and s1[0] <= p1[0] <= s2[0]:
                print("T")
            else:
                print("F")
        elif p1[1] == p2[1]:
            if s1[1] != p1[1]:
                print("F")
            elif p1[0] > s2[0] or p2[0] < s1[0]:
                print("F")
            else:
                print(T)
        elif min(p1[1], p2[1]) <= s1[1] <= max(p1[1], p2[1]):
            x = slope2(p1, p2)*(s1[1] - p1[1]) + p1[0]
            if s1[0]  <= x <= s2[0]:
                print("T")
            else:
                print('F')
        else:
            print("F")
    else:
        if s1[0] <= p1[0] <= s2[0] and min(s1[1], s2[1]) <= p1[1] <= max(s1[1], s2[1]):
            # 점1이 사각형 안
            print("T")
        elif s1[0] <= p2[0] <= s2[0] and min(s1[1], s2[1]) <= p2[1] <= max(s1[1], s2[1]):
            # 점2가 사각형 안
            print("T")
        elif p1 == p2:
            print("F")
        # 사각형이 존재하고 점이 두 개 존재하며 모두 밖
        # 위쪽
        # x = s1[0], y = min(s1[1], s2[1]) max(s1[1], s2[1])
        elif p1[0] == p2[0]:
            # 사각형 존재, 직선 세로
            if s1[0] <= p1[0] <= s2[0]:
                if min(p1[1], p2[1]) > max(s1[1], s2[1]) or max(p1[1], p2[1]) < min(s1[1], s2[1]):
                    print("F")
                else:
                    print("T")
            else:
                print("F")
        elif p1[1] == p2[1]:
            # 사각형 존재, 직선 가로
            if min(s1[1], s2[1]) <= p1[1] <= max(s1[1], s2[1]):
                if s2[0] < p1[0] or s1[0] > p2[0]:
                    print("F")
                else:
                    print("T")
            else:
                print("F")
        else:
            if p1[0] > s2[0] or p2[0] < s1[0] or min(p1[1], p2[1]) > max(s1[1], s2[1]) or max(p1[1], p2[1]) < min(s1[1], s2[1]):
                print("F")
            else:
                # 사각형 존재, 직선 대각선
                flag = False
                # 왼쪽
                if flag == False:
                    y = slope1(p1, p2)*(s1[0] - p1[0]) + p1[1]
                    if min(s1[1], s2[1]) <= y <= max(s1[1], s2[1]):
                        flag = True
                # 오른쪽
                if flag == False:
                    y = slope1(p1, p2)*(s2[0] - p1[0]) + p1[1]
                    if min(s1[1], s2[1]) <= y <= max(s1[1], s2[1]):
                        flag = True
                # 위
                if flag == False:
                    x = slope2(p1, p2)*(max(s1[1], s2[1]) - p1[1]) + p1[0]
                    if s1[0] <= x <= s2[0]:
                        flag = True
                # 아래
                if flag == False:
                    x = slope2(p1, p2)*(min(s1[1], s2[1]) - p1[1]) + p1[0]
                    if s1[0] <= x <= s2[0]:
                        flag = True
                        
                if flag:
                    print("T")
                else:
                    print("F")