from collections import deque
from sys import stdin, maxsize


def make_bridge():
    result = maxsize
    while bq:
        x, y, m = bq.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or m == b[nx][ny]:
                continue
            if b[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                b[nx][ny] = m
                bq.append((nx, ny, m))
            else:
                result = min(result, dist[x][y] + dist[nx][ny])
    print(result)


def get_local(x, y, m):
    q = deque([(x, y)])
    b[x][y] = m
    bq.append((x, y, m))
    while q:
        ax, ay = q.popleft()
        for k in range(4):
            nx, ny = ax + dx[k], ay + dy[k]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or b[nx][ny] != 1:
                continue
            b[nx][ny] = m
            q.append((nx, ny))
            bq.append((nx, ny, m))


if __name__ == '__main__':
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = int(stdin.readline())
    b = [list(map(int, stdin.readline().split())) for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    bq = deque([])
    cnt = 1

    for i, row in enumerate(b):
        for j, item in enumerate(row):
            if item == 1:
                cnt += 1
                get_local(i, j, cnt)
    make_bridge()

