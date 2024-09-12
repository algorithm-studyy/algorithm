from collections import deque

def bfs(i, j, arr, costs):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if costs[nx][ny] > costs[x][y] + arr[nx][ny]:
                    costs[nx][ny] = costs[x][y] + arr[nx][ny]
                    q.append((nx, ny))


if __name__ == "__main__":
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while True:
        n = int(input())
        if n == 0:
            exit(0)
        arr = [list(map(int, input().split())) for _ in range(n)]
        costs = [[int(1e9)] * n for _ in range(n)]

        costs[0][0] = arr[0][0]
        bfs(0, 0, arr, costs)

        print(costs[n - 1][n - 1])
