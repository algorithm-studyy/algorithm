# 동서남북 0이 저장된 칸의 개수만큼 높이가 줄어듦
# 한 덩어리 빙산이 주어질 때 두 덩어리 이상으로 분리되는 최초의 시간을 구해라

# BFS
# 1. 빙산 구하기 - 0이 아닌 애들 큐에 넣기
# 2. 큐를 한 번 모두 돌기
# 3. 0인 애들 빼고 큐에 다시 넣고,

from collections import deque
from sys import stdin


def check_visit(i, j, v):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or v[nx][ny]:
                continue
            if b[nx][ny] == 0:
                continue
            v[nx][ny] = True
            q.append((nx, ny))


def is_complete():
    visit = [[False] * m for _ in range(n)]
    result = 0
    for i, row in enumerate(b):
        for j, item in enumerate(row):
            if not visit[i][j] and item != 0:
                result += 1
                visit[i][j] = True
                check_visit(i, j, visit)
    if result >= 2:
        return True
    return False


def bfs():
    q = deque(get_ice())
    year = 0
    while q:
        if is_complete():
            return year
        for _ in range(len(q)):
            x, y, k = q.popleft()
            sub = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if b[nx][ny] == 0:
                    sub += 1
            k = max(0, k - sub)
            q.append((x, y, k))
        q = update_ice(q)
        year += 1
    return 0


def update_ice(q):
    result = deque([])
    while q:
        x, y, k = q.popleft()
        b[x][y] = k
        if b[x][y] > 0:
            result.append((x, y, k))
    return result


def get_ice():
    result = []
    for i, row in enumerate(b):
        for j, item in enumerate(row):
            if item != 0:
                result.append((i, j, item))
    return sorted(result, key=lambda x: x[2], reverse=True)


if __name__ == '__main__':
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n, m = map(int, stdin.readline().split())
    b = [list(map(int, stdin.readline().split())) for _ in range(n)]
    print(bfs())
