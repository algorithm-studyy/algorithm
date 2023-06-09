# 탈출문은 레버를 당겨서만 열 수 있다.
# 레버에 있는 곳에 먼저 간 후 탈출 문으로 가야함
# bfs를 사용
# 'S'에서 'L' 까지 거리 + 'L' 에서 'E'까지 거리 = answer

from collections import deque


def bfs(start, end, maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for i in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                q.append((i, j))
                visited[i][j] = True

    while q:
        x, y = q.popleft()

        if map[x][y] == end:
            return count

        for i in range(x):
            nx = i + dx[i]
            ny = i + dy[i]

            if 0 < nx < m and 0 < ny < n and maps[i][j] != 'X':
                q.append((i, j))
                count += 1
                visited[nx][ny] = True
    return -1


def solution(maps):
    path_to_l = bfs('S', 'L', maps)
    path_to_e = bfs('L', 'E', maps)

    answer = 0

    return answer