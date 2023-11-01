from sys import stdin
from collections import deque


def bfs(x, y):
    global result
    q = deque([(x, y)])
    num = 0
    while q:
        x, y = q.popleft()
        num += 1
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != 1 or visit[nx][ny]:
                continue
            visit[nx][ny] = True
            q.append((nx, ny))
    result = max(result, num)


if __name__ == '__main__':
    result = 0
    count = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n, m = map(int, stdin.readline().split())
    board = [list(list(map(int, stdin.readline().strip().split()))) for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == 1 and not visit[i][j]:
                count += 1
                visit[i][j] = True
                bfs(i, j)
    print(count, result, sep="\n")
