from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
count_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            count_list.append(bfs(graph, i, j))

count_list.sort()
print(len(count_list))
for i in range(len(count_list)):
    print(count_list[i])