import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    known = set(sys.stdin.readline().split()[1:])
    if known:
        parties = [[], []]
        for _ in range(M):
            tmp = set(sys.stdin.readline().split()[1:])
            if known & tmp:
                known = known.union(tmp)
                parties[0].append(tmp)
            else:
                parties[1].append(tmp)

        flag = True
        while flag:
            flag = False
            if parties[1]:
                for i, party in enumerate(parties[1]):
                    if party != 0 and known & party:
                        flag = True
                        known = known.union(party)
                        parties[0].append(party)
                        parties[1][i] = 0
            else:
                flag = False
                
        print(M - len(parties[0]))
        
    else:
        for _ in range(M):
            sys.stdin.readline()
        print(M)