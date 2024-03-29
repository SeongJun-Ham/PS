import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    meeting_info = []
    
    for _ in range(N):
        start, end = map(int, input().split())
        meeting_info.append((end, start))
    meeting_info.sort()
    
    ans = 0
    idx = 0
    cur_end = 0
    while idx < len(meeting_info):
        if meeting_info[idx][1] >= cur_end:
            ans +=1
            cur_end = meeting_info[idx][0]
        idx += 1
    
    print(ans)
