from sys import stdin
from collections import deque


def bfs(q):
    while q:
        ax, ay, az = q.popleft()
        for i in range(6):
            nx, ny, nz = ax + dx[i], ay + dy[i], az + dz[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if board[nx][ny][nz] != 0:
                continue
            q.append((nx, ny, nz))
            board[nx][ny][nz] = board[ax][ay][az] + 1


def get_board():
    result = []
    for x in range(h):
        result.append(list())
        for y in range(n):
            result[x].append(list(map(int, stdin.readline().split())))
    return result


def solution():
    result = 0
    q = deque([])
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 1:
                    q.append((i, j, k))
    bfs(q)
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 0:
                    return -1
                result = max(result, board[i][j][k] - 1)
    return result


if __name__ == '__main__':
    dx = [0, 0, -1, 1, 0, 0]
    dy = [-1, 1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    m, n, h = map(int, stdin.readline().split())
    board = get_board()
    print(solution())
