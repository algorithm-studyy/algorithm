from collections import deque
from sys import stdin


def set_board():
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        b[y][x] = 1


def bfs(x, y):
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or b[ny][nx] != 1:
                continue
            b[ny][nx] = 2
            q.append((ny, nx))


def iterate():
    count = 0
    for i, row in enumerate(b):
        for j, item in enumerate(row):
            if item == 1:
                b[i][j] = 2
                count += 1
                bfs(j, i)
    print(count)


if __name__ == '__main__':
    t = int(stdin.readline())
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for _ in range(t):
        m, n, k = map(int, stdin.readline().split())
        b = [[0] * m for _ in range(n)]
        set_board()
        iterate()

