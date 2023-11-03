from collections import deque
from sys import stdin, maxsize


def bfs():
    q = deque([[0, 0]])
    c[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or c[nx][ny] != -1:
                continue
            if b[nx][ny] == 1:
                c[nx][ny] = c[x][y] + 1
                q.append([nx, ny])
            else:
                c[nx][ny] = c[x][y]
                q.appendleft([nx, ny])


if __name__ == '__main__':
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    m, n = map(int, stdin.readline().split())
    b = [list(map(int, list(stdin.readline().strip()))) for _ in range(n)]
    c = [[-1] * m for _ in range(n)]
    bfs()
    print(c[n - 1][m - 1])

