# 핵심은 dist를 두 개로 나눠서 벽을 부수고 간 거리, 안 부수고 간 거리를 측정하는게 중요

from collections import deque
from sys import stdin


def bfs():
    q = deque([(0, 0, 0)])
    while q:
        x, y, t = q.popleft()
        if x == n - 1 and y == m - 1:
            print(dist[x][y][t])
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0 and dist[nx][ny][t] == 0:
                dist[nx][ny][t] = dist[x][y][t] + 1
                q.append((nx, ny, t))
            elif board[nx][ny] == 1 and t == 0:
                dist[nx][ny][t + 1] = dist[x][y][t] + 1
                q.append((nx, ny, t + 1))
    print(-1)


if __name__ == '__main__':
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n, m = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().strip())) for _ in range(n)]
    dist = [[[0, 0] for _ in range(m)] for _ in range(n)]
    dist[0][0][0] = 1
    bfs()
    for row in dist:
        print(*row)
