from sys import stdin
from collections import deque


def bfs(x, y):
    cnt = 1
    q = deque([[x, y]])
    b[x][y] = 0
    while q:
        nx, ny = q.popleft()
        for k in range(4):
            new_x, new_y = nx + dx[k], ny + dy[k]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n or not b[new_x][new_y]:
                continue
            b[new_x][new_y] = 0
            cnt += 1
            q.append([new_x, new_y])
    return cnt


if __name__ == '__main__':
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    n = int(stdin.readline())
    b = [list(map(int, list(stdin.readline().strip()))) for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(n):
            if b[i][j]:
                answer.append(bfs(i, j))
    print(len(answer))
    print(*sorted(answer), sep='\n', end='')
