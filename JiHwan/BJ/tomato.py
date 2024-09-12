# 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶다

from collections import deque


def bfs(x, y):
    q.append((x, y))
    count = 0
    while q:
        t, a = q.popleft()

        for i in range(4):
            nx = t + dx[i]
            ny = a + dy[i]

            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                count += 1
                box[nx][ny] = box[t][a] + 1
                q.append((nx, ny))


if __name__ == "__main__":
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(m)]
    q = deque()
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                bfs(i, j)

    for i in box:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        answer = max(i) - 1

    print(answer)
