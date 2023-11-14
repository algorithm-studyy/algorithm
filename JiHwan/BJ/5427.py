from collections import deque
import sys


def bfs():
    time = 0

    while fire:
        time += 1
        fx, fy = fire.popleft()

        for i in range(4):
            nfx = fx + dx[i]
            nfy = fy + dy[i]

            if 0 <= nfx < n and 0 <= nfy < m:
                if matrix[nfx][nfy] == "." and visited[nfx][nfy] == False:
                    matrix[nfx][nfy] = "*"
                    visited[nfx][nfy] = True

    while q:
        time += 1
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == "." and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            else:
                return time
    return "IMPOSSIBLE"


if __name__ == "__main__":
    t = int(input())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(t):
        m, n = map(int, input().split())
        q = deque()
        fire = deque()

        matrix = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '@':
                    visited[i][j] = True
                    q.append((i, j))
                if matrix[i][j] == '*':
                    visited[i][j] = True
                    fire.append((i, j))
        print(bfs())
