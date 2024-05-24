import sys
input = sys.stdin.readline

def binary_search(target, arr):
    left = 0
    right = len(arr)-1
    mid = (left+right)//2
    while right - left > 1:
        if arr[mid] >= target:
            right = mid
        else:
            left = mid
        mid = (left+right)//2
    return mid+1


def LIS(seq):
    A = [0]
    B = [0]
    for n in range(N):
        if A[-1] < seq[n]:
            A.append(seq[n])
            B.append(seq[n])
        elif A[-1] > seq[n]:
            idx = binary_search(seq[n], A)
            A[idx] = seq[n]
            if idx == len(A)-1:
                B = A[:]
    return B


if __name__ == "__main__":
    N = int(input())
    sequence = list(map(int, input().split()))
    
    ans = LIS(sequence)
    print(len(ans)-1)
