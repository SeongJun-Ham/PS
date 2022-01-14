import sys

T = int(sys.stdin.readline())

def turnU(command, center, F, R, B, L):
    if command == "+":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[3], center[1], center[5], center[7]
        BC[0], BC[2], BC[8], BC[6] = center[6], center[0], center[2], center[8]
        s = [0 for i in range(9)]
        s[0:3] = F[0:3]
        F[0:3] = R[0:3]
        R[0:3] = B[0:3]
        B[0:3] = L[0:3]
        L[0:3] = s[0:3]
    elif command == "-":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[5], center[7], center[3], center[1]
        BC[0], BC[2], BC[8], BC[6] = center[2], center[8], center[6], center[0]
        s = [0 for i in range(9)]
        s[0:3] = F[0:3]
        F[0:3] = L[0:3]
        L[0:3] = B[0:3]
        B[0:3] = R[0:3]
        R[0:3] = s[0:3]
    return center, F, R, B, L

def turnD(command, center, F, R, B, L):
    if command == "+":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[3], center[1], center[5], center[7]
        BC[0], BC[2], BC[8], BC[6] = center[6], center[0], center[2], center[8]
        s = [0 for i in range(9)]
        s[6:9] = F[6:9]
        F[6:9] = L[6:9]
        L[6:9] = B[6:9]
        B[6:9] = R[6:9]
        R[6:9] = s[6:9]
    elif command == "-":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[5], center[7], center[3], center[1]
        BC[0], BC[2], BC[8], BC[6] = center[2], center[8], center[6], center[0]
        s = [0 for i in range(9)]
        s[6:9] = F[6:9]
        F[6:9] = R[6:9]
        R[6:9] = B[6:9]
        B[6:9] = L[6:9]
        L[6:9] = s[6:9]
    return center, F, R, B, L

def turnL(command, center, F, U, B, D):
    if command == "+":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[3], center[1], center[5], center[7]
        BC[0], BC[2], BC[8], BC[6] = center[6], center[0], center[2], center[8]
        s = [0 for i in range(9)]
        s[0], s[3], s[6] = F[0], F[3], F[6]
        F[0], F[3], F[6] = U[0], U[3], U[6]
        U[0], U[3], U[6] = B[8], B[5], B[2]
        B[8], B[5], B[2] = D[0], D[3], D[6]
        D[0], D[3], D[6] = s[0], s[3], s[6]
    elif command == "-":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[5], center[7], center[3], center[1]
        BC[0], BC[2], BC[8], BC[6] = center[2], center[8], center[6], center[0]
        s = [0 for i in range(9)]
        s[0], s[3], s[6] = F[0], F[3], F[6]
        F[0], F[3], F[6] = D[0], D[3], D[6]
        D[0], D[3], D[6] = B[8], B[5], B[2]
        B[8], B[5], B[2] = U[0], U[3], U[6]
        U[0], U[3], U[6] = s[0], s[3], s[6]
    return center, F, U, B, D
        
def turnR(command, center, F, U, B, D):
    if command == "+":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[3], center[1], center[5], center[7]
        BC[0], BC[2], BC[8], BC[6] = center[6], center[0], center[2], center[8]
        s = [0 for i in range(9)]
        s[2], s[5], s[8] = F[2], F[5], F[8]
        F[2], F[5], F[8] = D[2], D[5], D[8]
        D[2], D[5], D[8] = B[6], B[3], B[0]
        B[6], B[3], B[0] = U[2], U[5], U[8]
        U[2], U[5], U[8] = s[2], s[5], s[8]
    elif command == "-":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[5], center[7], center[3], center[1]
        BC[0], BC[2], BC[8], BC[6] = center[2], center[8], center[6], center[0]
        s = [0 for i in range(9)]
        s[2], s[5], s[8] = F[2], F[5], F[8]
        F[2], F[5], F[8] = U[2], U[5], U[8]
        U[2], U[5], U[8] = B[6], B[3], B[0]
        B[6], B[3], B[0] = D[2], D[5], D[8]
        D[2], D[5], D[8] = s[2], s[5], s[8]
    return center, F, U, B, D

def turnF(command, center, U, R, D, L):
    if command == "+":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[3], center[1], center[5], center[7]
        BC[0], BC[2], BC[8], BC[6] = center[6], center[0], center[2], center[8]
        s = [0 for i in range(9)]
        s[6], s[7], s[8] = U[6], U[7], U[8]
        U[6], U[7], U[8] = L[8], L[5], L[2]
        L[8], L[5], L[2] = D[2], D[1], D[0]
        D[2], D[1], D[0] = R[0], R[3], R[6]
        R[0], R[3], R[6] = s[6], s[7], s[8]
    elif command == "-":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[5], center[7], center[3], center[1]
        BC[0], BC[2], BC[8], BC[6] = center[2], center[8], center[6], center[0]
        s = [0 for i in range(9)]
        s[6], s[7], s[8] = U[6], U[7], U[8]
        U[6], U[7], U[8] = R[0], R[3], R[6]
        R[0], R[3], R[6] = D[2], D[1], D[0]
        D[2], D[1], D[0] = L[8], L[5], L[2]
        L[8], L[5], L[2] = s[6], s[7], s[8]
    return center, U, R, D, L
        
def turnB(command, center, U, R, D, L):
    if command == "+":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[3], center[1], center[5], center[7]
        BC[0], BC[2], BC[8], BC[6] = center[6], center[0], center[2], center[8]
        s = [0 for i in range(9)]
        s[0], s[1], s[2] = U[0], U[1], U[2]
        U[0], U[1], U[2] = R[2], R[5], R[8]
        R[2], R[5], R[8] = D[8], D[7], D[6]
        D[8], D[7], D[6] = L[6], L[3], L[0]
        L[6], L[3], L[0] = s[0], s[1], s[2]
    elif command == "-":
        BC = center
        BC[1], BC[5], BC[7], BC[3] = center[5], center[7], center[3], center[1]
        BC[0], BC[2], BC[8], BC[6] = center[2], center[8], center[6], center[0]
        s = [0 for i in range(9)]
        s[0], s[1], s[2] = U[0], U[1], U[2]
        U[0], U[1], U[2] = L[6], L[3], L[0]
        L[6], L[3], L[0] = D[8], D[7], D[6]
        D[8], D[7], D[6] = R[2], R[5], R[8]
        R[2], R[5], R[8] = s[0], s[1], s[2]
    return center, U, R, D, L
        
for i in range(T):
    U = ['w' for i in range(9)]
    D = ['y' for i in range(9)]
    F = ['r' for i in range(9)]
    B = ['o' for i in range(9)]
    L = ['g' for i in range(9)]
    R = ['b' for i in range(9)]
    
    n = int(sys.stdin.readline()[:-1])
    funcList = list(sys.stdin.readline().split())
    for j in funcList:
        if j[0] == "U":
            U, F, R, B, L = turnU(j[1], U, F, R, B, L)
        elif j[0] == "D":
            D, F, R, B, L = turnD(j[1], D, F, R, B, L)
        elif j[0] == "L":
            L, F, U, B, D = turnL(j[1], L, F, U, B, D)
        elif j[0] == "R":
            R, F, U, B, D = turnR(j[1], R, F, U, B, D)
        elif j[0] == "F":
            F, U, R, D, L = turnF(j[1], F, U, R, D, L)
        elif j[0] == "B":
            B, U, R, D, L = turnB(j[1], B, U, R, D, L)
    for k in range(3):
        print("{}{}{}".format(U[k*3], U[k*3 + 1], U[k*3 + 2]))