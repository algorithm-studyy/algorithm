from sys import stdin
from collections import deque


def bfs():
    q = deque([(0, 0, 0)])
    while q:
        x, y, c = q.popleft()
        if x == n - 1 and y == m - 1:
            print(dist[x][y][c])
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0 and dist[nx][ny][c] == 0:
                dist[nx][ny][c] = dist[x][y][c] + 1
                q.append((nx, ny, c))
            elif board[nx][ny] == 1 and c == 0:
                dist[nx][ny][c + 1] = dist[x][y][c] + 1
                q.append((nx, ny, c + 1))

    print(-1)


def get_dist():
    result = []
    for i in range(n):
        result.append([])
        for _ in range(m):
            result[i].append([0, 0])
    return result


if __name__ == '__main__':
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().strip())) for _ in range(n)]
    dist = get_dist()
    dist[0][0][0] = 1
    bfs()
