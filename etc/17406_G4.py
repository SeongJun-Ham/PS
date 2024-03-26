import sys
from itertools import permutations


def rotate(axis: int, radius: int, array: list) -> list:
    result = [[0 for _ in range(2 * radius + 1)] for _ in range(2 * radius + 1)]
    result[radius][radius] = array[axis[0]][axis[1]]
    vx, vy = [1, 0, -1, 0, 1], [0, 1, 0, -1, 0]
    dx, dy = [-1, 1, 1, -1], [-1, -1, 1, 1]
    for r in range(1, radius + 1):
        init = (radius - axis[0], radius - axis[1])
        for i in range(4):
            # starting point
            sp = (axis[0] + r * dy[i], axis[1] + r * dx[i])
            for j in range(2 * r):
                bpy = sp[0] + j * vy[i]
                bpx = sp[1] + j * vx[i]
                apy = sp[0] + init[0] + (j+1) * vy[i]
                apx = sp[1] + init[1] + (j+1) * vx[i]
                result[apy][apx] = array[bpy][bpx]

    for i in range(2*radius+1):
        array[axis[0] + i - radius][axis[1] - radius:axis[1] + radius + 1] = result[i]

    return array


def search_min_value(array: list) -> int:
    result = sum(array[0])
    for i in range(1, len(array)):
        result = min(result, sum(array[i]))
    return result


if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    func = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    orders = [i for i in range(K)]
    ans = 5001
    for order in permutations(orders):
        result = [list(arr[i]) for i in range(N)]
        for ord in order:
            result = rotate((func[ord][0] - 1, func[ord][1] - 1), func[ord][2], result)
        ans = min(ans, search_min_value(result))

    print(ans)
