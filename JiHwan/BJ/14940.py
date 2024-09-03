from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    start_x, start_y = 0, 0
    wall_list = []
    visited = [[-1] * m for _ in range(n)]

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 2:
                start_x, start_y = i, j
            if graph[i][j] == 0:
                wall_list.append((i, j))
    visited[start_x][start_y] = 0

    for wall in wall_list:
        visited[wall[0]][wall[1]] = 0

    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    for i in range(n):
        print(" ".join(map(str, visited[i])))

