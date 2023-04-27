from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(maps):
    q = deque([[0, 0]])
    n, m = len(maps), len(maps[0])
    while q:
        y, x = q.popleft()
        if y == n - 1 and x == m - 1:
            return maps[y][x]
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx >= m or nx < 0 or ny >= n or ny < 0 or maps[ny][nx] != 1:
                continue
            maps[ny][nx] += maps[y][x]
            q.append([ny, nx])
    return -1
