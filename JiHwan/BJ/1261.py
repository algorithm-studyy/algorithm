from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= M:
            continue

        if not visited[nx][ny]:
            if graph[nx][ny] == 0:
                graph[nx][ny] == visited[x][y]
                queue.append([nx, ny])
            else:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])


if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    graph = []
    for i in range(M):
        graph.append(list(map(int, input())))

    visited = [[-1] * N for _ in range(M)]
    bfs(0, 0)
    print(visited[N-1][M-1])
