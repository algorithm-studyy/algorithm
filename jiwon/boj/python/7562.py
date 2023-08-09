from collections import deque
from sys import stdin


def bfs(bx, by):
    q = deque([[bx, by]])
    v[bx][by] = 0
    while q:
        tx, ty = q.popleft()
        if tx == ax and ty == ay:
            return
        for i in range(8):
            nx, ny = tx + dx[i], ty + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or v[nx].get(ny):
                continue
            q.append([nx, ny])
            v[nx][ny] = v[tx][ty] + 1


if __name__ == '__main__':
    t = int(stdin.readline())
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    for _ in range(t):
        n = int(stdin.readline())
        v = {}
        for j in range(n):
            v[j] = {}
        x, y = map(int, stdin.readline().split(' '))
        ax, ay = map(int, stdin.readline().split(' '))
        bfs(x, y)
        print(v[ax][ay])
