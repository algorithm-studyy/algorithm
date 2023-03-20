from collections import deque
from sys import stdin


def print_answer():
    max_val = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                print(-1)
                return
            max_val = max(b[i][j], max_val)

    print(max_val - 1)


def bfs():
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            nx, ny = ax + dx[i], ay + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or b[nx][ny] != 0:
                continue
            b[nx][ny] = b[ax][ay] + 1
            q.append([nx, ny])


if __name__ == '__main__':
    q = deque([])
    m, n = map(int, stdin.readline().split(' '))
    b = [list(map(int, stdin.readline().split(' '))) for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for r in range(n):
        for c in range(m):
            if b[r][c] == 1:
                q.append([r, c])
    bfs()
    print_answer()
