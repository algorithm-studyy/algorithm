from sys import stdin
from collections import deque


def bfs():
    fires = find_fire()
    start = find_start()
    q = deque([start]) if not fires else deque([*fires, start])
    while q:
        x, y, k = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                if k == '@':
                    print(dist[x][y] + 1)
                    return
                continue
            if board[nx][ny] != '.' or dist[nx][ny] != 0:
                continue
            if k == '*':
                board[nx][ny] = '*'
            elif k == '@':
                dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny, k))
    print('IMPOSSIBLE')


def find_fire():
    result = []
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == '*':
                result.append((i, j, '*'))
    return result


def find_start():
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == '@':
                return i, j, '@'
    return None


if __name__ == '__main__':
    t = int(stdin.readline())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(t):
        w, h = map(int, stdin.readline().split())
        board = [list(stdin.readline().strip()) for _ in range(h)]
        dist = [[0] * w for _ in range(h)]
        bfs()
