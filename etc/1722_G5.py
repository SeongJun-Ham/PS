N = int(input())
arr = list(map(int, input().split()))

def fac(n):
	m = 1
	for i in range(1, n+1):
		m *= i
	return m

if N == 1:
	print(1)
	
else:
    K = [i+1 for i in range(N)]
    if arr[0] == 1:
        result = []
        for i in range(N):
            T = fac(N - 1 - i)
            result.append(K.pop((arr[1] - 1)//T))
            arr[1] = (arr[1] - 1)%T + 1
        print(" ".join(map(str, result)))
    else:
        result = 0
        arr.pop(0)
        for i in range(N - 2):
            T = fac(N - 1 - i)
            num = K.index(arr[0])
            result += T*num
            K.pop(K.index(arr[0]))
            arr.pop(0)
        if arr[0] > arr[1]:
            print(result + 2)
        else:
            print(result + 1)