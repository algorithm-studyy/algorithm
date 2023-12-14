from collections import deque


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny][z] and not graph[nx][ny]:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append([nx, ny, z])
        if z < k:
            for i in range(8):
                h_nx = x + horse_x[i]
                h_ny = y + horse_y[i]
                if 0 <= h_nx < m and 0 <= h_ny < n and not graph[h_nx][h_ny] and not visited[h_nx][h_ny][z + 1]:
                    visited[h_nx][h_ny][z + 1] = visited[x][y][z] + 1
                    q.append([h_nx, h_ny, z + 1])
    return -1


if __name__ == "__main__":
    k = int(input())
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    dx = [1, -1, 0, 0]  # 상하좌우
    dy = [0, 0, 1, -1]
    horse_x = [-1, -2, -2, -1, 1, 2, 2, 1]
    horse_y = [-2, -1, 1, 2, 2, 1, -1, -2]  # 체스 나이트 이동
    visited = [[[0] * (k + 1) for _ in range(n)] for _ in range(m)]  # visited[행][열][나이트 이동 수]
    print(bfs())
