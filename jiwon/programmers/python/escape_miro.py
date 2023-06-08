# 1. L이 E가는 길에 있는 경우 -> E까지의 수를 센다
# 2. L이 E가는 도중에 없고, L에 갈 수 있는 경우 -> L + E
# L이 도중에 있는 어떻게 확인할까?
# 3. L에 갈 수 없는 경우, E에 갈 수 없는 경우 -> -1
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def find_mark(m, mark):
    for i, row in enumerate(m):
        for j, item in enumerate(row):
            if item == mark:
                return i, j


def solution(m):
    start, lever, ext = find_mark(m, 'S'), find_mark(m, 'L'), find_mark(m, 'E')
    print(start, lever, ext)
    r, c = len(m), len(m[0])
    v = [[-1] * c for _ in range(r)]
    q = deque([start])
    v[start[0]][start[1]] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny >= r or ny < 0 or nx >= c or nx < 0 or m[ny][nx] == 'X' or v[ny][nx] != -1:
                continue
            v[ny][nx] = v[y][x] + 1
            q.append((ny, nx))
    if v[lever[0]][lever[1]] == -1 or v[ext[0]][ext[1]] == -1:
        return -1
    return v[ext[0]][ext[1]]
