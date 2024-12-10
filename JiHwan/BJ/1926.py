# 1인 값만 bfs 진행
# 인접한 1의 개수를 arr라는 list에 담음
# arr의 길이와 최대값 출력
from collections import deque


def bfs(a, b):
    count = 0
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        count += 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return count


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    arr = []

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                w = bfs(i, j)
                arr.append(w)
    print(len(arr))
    print(max(arr) if arr else 0)
