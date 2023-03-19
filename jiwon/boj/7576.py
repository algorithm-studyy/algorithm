from collections import deque
from sys import stdin


def print_answer():
    max_val = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0 and cost[i][j] == 1001:
                print(-1)
                return
            elif cost[i][j] == 1001:
                continue
            max_val = max(cost[i][j], max_val)

    print(max_val - 1)


def bfs(x, y):
    q = deque([[x, y]])
    visit[x][y] = True
    cost[x][y] = 1
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            nx, ny = ax + dx[i], ay + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or b[nx][ny] == -1 or visit[nx][ny]:
                continue
            cost[nx][ny] = min(cost[nx][ny], cost[ax][ay] + 1)
            visit[nx][ny] = True
            q.append([nx, ny])


if __name__ == '__main__':
    m, n = map(int, stdin.readline().split(' '))
    b = [list(map(int, stdin.readline().split(' '))) for _ in range(n)]
    cost = [[1001] * m for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    min_val = 1001
    for r in range(n):
        for c in range(m):
            if b[r][c] == 1:
                visit = [[False] * m for _ in range(n)]
                bfs(r, c)

    print_answer()
