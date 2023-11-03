# 이동 위치가 불인 곳을 지우기

from sys import stdin
from collections import deque


def find_start_and_fire():
    fire = []
    start = None
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == 'J':
                start = (i, j, 'J')
            elif item == 'F':
                fire.append((i, j, 'F'))
    return start, fire


def bfs():
    start, fire = find_start_and_fire()
    q = deque([*fire, start]) if fire else deque([start])
    while q:
        x, y, t = q.popleft()
        if t == 'J' and (x == r - 1 or y == c - 1 or x == 0 or y == 0):
            return dist[x][y] + 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if board[nx][ny] == 'F' or board[nx][ny] == '#' or dist[nx][ny] != 0:
                continue
            if t == 'J':
                dist[nx][ny] = dist[x][y] + 1
            elif t == 'F':
                board[nx][ny] = 'F'
            q.append((nx, ny, t))
    return "IMPOSSIBLE"


if __name__ == '__main__':
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    r, c = map(int, stdin.readline().split())
    board = [list(stdin.readline().strip()) for _ in range(r)]
    dist = [[0] * c for _ in range(r)]
    print(bfs())

