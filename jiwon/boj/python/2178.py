from sys import stdin
from sys import maxsize
from collections import deque


def bfs(x, y):
    q = deque([[x, y]])
    b[x][y] = 0
    c[x][y] = 1
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            new_x, new_y = nx + dx[i], ny + dy[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m or not b[new_x][new_y]:
                continue
            b[new_x][new_y] = 0
            c[new_x][new_y] = min(c[nx][ny] + 1, c[new_x][new_y])
            q.append([new_x, new_y])
    print(c[n - 1][m - 1])


if __name__ == '__main__':
    n, m = map(int, stdin.readline().split(' '))
    b = [list(map(int, list(stdin.readline().strip()))) for _ in range(n)]
    c = [[maxsize] * m for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    bfs(0, 0)

