from collections import deque


n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 0

    while q:
        a, b = q.popleft()
        print(a, b, n, m)
        if a == n - 1 and b == m - 1:
            return graph[a][b]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dx[i]
            print(nx, ny)

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0 and count == 0:
                count += 1
                visited[nx][ny] = 1
                graph[nx][ny] = graph[a][b] + 1
                q.append((x, y))
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                graph[nx][ny] = graph[a][b] + 1
                q.append((x, y))
    print(graph)
    return -1


print(bfs(0, 0))



