from collections import deque


def bfs(x, y):
    visited[x][y] == 1
    now_color = a[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 < nx < N and 0 < ny < N:
            if visited[nx][ny] == 0:
                if a[nx][ny] == now_color:
                    bfs(nx, ny)


if __name__ == "__main__":
    N = int(input())
    a = [list(input()) for _ in range(N)]
    q = deque()
    visited = [[0] * N for _ in range(N)]
    pre_count, post_count = 0, 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i, j)
                pre_count += 1

    for i in range(N):
        for j in range(N):
            if a[i][j] == 'R':
                a[i][j] = 'G'

    visited = [[0] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                dfs(i, j)
                post_count += 1

    print(pre_count, post_count)
