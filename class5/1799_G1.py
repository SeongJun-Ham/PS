import sys

def checkOverlap(check1, check2, cdn):
    if check1[cdn[0] - cdn[1]] == 0 and check2[cdn[0] + cdn[1]] == 0:
        return False
    else:
        return True
    
def main(check1, check2, possible, max_value):
    count = 1
    for m in range(len(possible)):
        if len(possible) - m > count:
            stack = [(m, 1)]
            while stack:
                flag = True
                current = stack[-1]
                cdn = possible[current[0]]
                check1[cdn[0] - cdn[1]] = 1
                check2[cdn[0] + cdn[1]] = 1
                for k in range(len(possible)-1, current[0], -1): 
                    K = possible[k]
                    if not checkOverlap(check1, check2, K):
                        stack.append((k, current[1] + 1))
                        flag = False
                
                if flag:
                    while stack:
                        S = stack.pop()
                        count = max(count, S[1])
                        if count == max_value:
                            return count
                        T = possible[S[0]]
                        check1[T[0] - T[1]] = 0
                        check2[T[0] + T[1]] = 0
                        
                        if stack:
                            if S[1] == stack[-1][1]:
                                break
                            
    return count
    

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    possibleB = []
    possibleW = []

    for c in range(N**2):
        cdn = divmod(c, N)
        if arr[cdn[0]][cdn[1]] == 1:
            if (cdn[0] + cdn[1]) % 2 == 0:
                possibleB.append(cdn)
            elif (cdn[0] + cdn[1]) % 2 == 1:
                possibleW.append(cdn)
                
    if len(possibleB) + len(possibleW) == 0:
        print(0)
    else:
        max_count = 0
        if len(possibleB) != 0:
            check1, check2 = [0]*(2*N-1), [0]*(2*N-1)
            max_count += main(check1, check2, possibleB, N-1)
            
        if len(possibleW) != 0:
            check1, check2 = [0]*(2*N-1), [0]*(2*N-1)
            max_count += main(check1, check2, possibleW, N)

        print(max_count)