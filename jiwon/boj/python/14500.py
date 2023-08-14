from sys import stdin

answer = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def is_h(x, y):
    global answer
    for c in range(4):
        v = b[y][x]
        for idx in range(4):
            if c == idx:
                continue
            nx, ny = x + dx[idx], y + dy[idx]
            if 0 > nx or nx >= m or ny < 0 or ny >= n:
                continue
            v += b[ny][nx]
            answer = max(answer, v)


def dfs(d, v, x, y):
    global answer
    if answer >= v + max_value * (3 - d):
        return
    if d == 3:
        answer = max(answer, v)
        return
    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]
        if 0 > nx or nx >= m or ny < 0 or ny >= n or visit[ny][nx]:
            continue
        visit[y][x] = True
        dfs(d + 1, v + b[ny][nx], nx, ny)
        visit[ny][nx] = False


n, m = map(int, stdin.readline().split())
b = [list(map(int, stdin.readline().split())) for _ in range(n)]
visit = [[False] * len(row) for row in b]
max_value = max(map(max, b))
for i, row in enumerate(b):
    for j, col in enumerate(row):
        visit[i][j] = True
        dfs(0, col, j, i)
        visit[i][j] = False
        is_h(j, i)

print(answer)
