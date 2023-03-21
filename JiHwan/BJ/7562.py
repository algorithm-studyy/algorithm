from collections import deque

N = int(input())

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]


def bfs():
    queue = deque()
    queue.append((sX, sY))
    while queue:
        x, y = queue.popleft()
        if x == eX and y == eY:
            return graph[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


if __name__ == "__main__":
    for _ in range(N):
        l = int(input())
        graph = [[0]*l for _ in range(l)]
        sX, sY = map(int, input().split(" "))
        eX, eY = map(int, input().split(" "))
        graph[sX][sY] = 1
        print(bfs())


