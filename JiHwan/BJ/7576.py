from collections import deque


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
        if N > nx >= 0 == graph[nx][ny] and 0 <= ny < M:
