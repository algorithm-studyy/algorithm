from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    cur = arr[y][x]
    arr[y][x] = 1
    count = 0
    while q:
        y, x = q.popleft()
        count += 1
        for i in range(4):
            n_dy = y + dy[i]
            n_dx = x + dx[i]
            if (0 <= n_dy < m) and (0 <= n_dx < n) and arr[n_dy][n_dx] == cur:
                q.append((n_dy, n_dx))
                arr[n_dy][n_dx] = 1
    return count


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
                w_cnt += bfs(i, j) ** 2
            elif arr[i][j] == 'B':
                b_cnt += bfs(i, j) ** 2

    print(w_cnt)
    print(b_cnt)





