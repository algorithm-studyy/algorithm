from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    cur = arr[y][x]


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for _ in range(m):
        arr.append(list(input().strip()))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    w_cnt = 0
    b_cnt = 0

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 'W':
                w_cnt += bfs(i, j)
            elif arr[i][j] == 'B':
                b_cnt += bfs(i, j)







