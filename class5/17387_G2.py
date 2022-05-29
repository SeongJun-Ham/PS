import math as m
import cmath as c

L1 = tuple(map(int, input().split()))
P1 = min((L1[0], L1[1]), (L1[2], L1[3]))
P2 = max((L1[0], L1[1]), (L1[2], L1[3]))
L2 = tuple(map(int, input().split()))
P3 = min((L2[0], L2[1]), (L2[2], L2[3]))
P4 = max((L2[0], L2[1]), (L2[2], L2[3]))

def slope(point1, point2):
    return ((point2[1] - point1[1])/(point2[0] - point1[0]))

if P1 == P3 or P1 == P4 or P2 == P3 or P2 == P4:
    print(1)
    
elif P1 == P2 and P3 == P4:
    if P1 == P3:
        print(1)
    else:
        print(0)    
        
elif P1 == P2:
    if P1[0] < P3[0] or P4[0] < P1[0]:
        print(0)
    else:
        if round(slope(P3, P4)*(P1[0] - P3[0]), 10) + P3[1] == P1[1]:
            print(1)
        else:
            print(0)
    
elif P3 == P4:
    if P3[0] < P1[0] or P2[0] < P3[0]:
        print(0)
    else:
        if round(slope(P1, P2)*(P3[0] - P1[0]), 10) + P1[1] == P3[1]:
            print(1)
        else:
            print(0)
    
else:
    r = abs(P2[0] + 1j*P2[1] - P1[0] - 1j*P1[1])
    p1 = 0
    p2 = (P2[0] + 1j*P2[1] - P1[0] - 1j*P1[1])/r
    p3 = (P3[0] + 1j*P3[1] - P1[0] - 1j*P1[1])/r
    p4 = (P4[0] + 1j*P4[1] - P1[0] - 1j*P1[1])/r

    theta = c.phase(p2)
    k = m.cos(theta) + 1j*m.sin(theta)
    p2 /= k
    p3 /= k
    p4 /= k
    p2 = round(p2.real, 10) + 1j*round(p2.imag, 10)
    p3 = round(p3.real, 10) + 1j*round(p3.imag, 10)
    p4 = round(p4.real, 10) + 1j*round(p4.imag, 10)

    x1, y1 = p3.real, p3.imag
    x2, y2 = p4.real, p4.imag

    if x1 == x2:
        if 0 <= x1 <= 1 and y1*y2 <= 0:
            print(1)
        else:
            print(0)
    elif y1 == y2:
        if y1 == 0:
            if x1 > 1 and x2 > 1:
                print(0)
            elif x1 < 0 and x2 < 0:
                print(0)
            else:
                print(1)
        else:
            print(0)
    else:
        slope = (x2 - x1)/(y2 - y1)
        x = round(slope*(-p3.imag), 10) + p3.real
        if 0 <= x <= 1 and y1*y2 <= 0:
            print(1)
        else:
            print(0)