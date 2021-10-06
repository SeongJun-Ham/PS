import sys

T = int(sys.stdin.readline())
result = ""

for i in range(T):
    k = int(sys.stdin.readline())
    Queue = []
    for i in range(k):
        func, num = map(str, sys.stdin.readline().split())
        num = int(num)
        if func == "I":
            if Queue:
                if Queue[0] >= num:
                    Queue.insert(0, num)
                elif Queue[len(Queue) - 1] <= num:
                    Queue.append(num)
                else:
                    start = 0
                    end = len(Queue) - 1
                    while True:
                        mid = (start + end) // 2
                        if num == Queue[mid]:
                            Queue.insert(mid, num)
                            break
                        elif num > Queue[mid]:
                            start = mid
                        elif num < Queue[mid]:
                            end = mid

                        if end - start == 1:
                            Queue.insert(end, num)
                            break
            else:
                Queue.append(num)

        else:
            if Queue:
                if num == 1:
                    k = Queue.pop()
                elif num == -1:
                    k = Queue.pop(0)
    
    if Queue:
        result += "{} {}\n".format(Queue[len(Queue) - 1],Queue[0])
    else:
        result += "EMPTY\n"

print(result[:-1])