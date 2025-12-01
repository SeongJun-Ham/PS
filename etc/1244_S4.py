N = int(input())

s_arr = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    s, num = map(int, input().split())
    idx = num-1

    if s == 1:
        while idx < N:
            s_arr[idx] = -1*s_arr[idx]+1
            idx += num

    elif s == 2:
        s_arr[idx] = -1*s_arr[idx]+1
        for i in range(1, N):
            if idx-i < 0 or idx+i >= N:
                break

            if s_arr[idx+i] == s_arr[idx-i]:
                s_arr[idx+i] = -1*s_arr[idx+i]+1
                s_arr[idx-i] = -1*s_arr[idx-i]+1
            else:
                break

i=-1
for i in range(len(s_arr)//20):
    print(" ".join(map(str, s_arr[20*i:20*(i+1)])))
print(" ".join(map(str, s_arr[20*(i+1):])))