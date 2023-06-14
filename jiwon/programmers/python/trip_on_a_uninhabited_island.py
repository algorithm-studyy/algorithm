from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(y, x, maps, v):
    result = int(maps[y][x])
    n, m = len(maps), len(maps[0])
    q = deque([[x, y]])
    v[y][x] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or v[ny][nx] or maps[ny][nx] == 'X':
                continue
            result += int(maps[ny][nx])
            v[ny][nx] = True
            q.append((nx, ny))
    return result


def solution(maps):
    answer = []
    v = [[False] * len(maps[0]) for _ in range(len(maps))]
    for i, row in enumerate(maps):
        for j, item in enumerate(row):
            if not v[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i, j, maps, v))
    return sorted(answer) if answer else [-1]
