from collections import deque

dist = dict()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_max(land):
    answer = 0
    for i in range(len(land[0])):
        num = 0
        adder_numbers = set()
        for j in range(len(land)):
            if land[j][i] != 0 and land[j][i] in dist and land[j][i] not in adder_numbers:
                num += dist[land[j][i]]
                adder_numbers.add(land[j][i])
        answer = max(answer, num)
    return answer


def bfs(x, y, land, mark):
    q = deque([(x, y)])
    n, m = len(land), len(land[0])
    count = 0
    while q:
        count += 1
        ax, ay = q.popleft()
        dist[mark] = count
        for i in range(4):
            nx, ny = ax + dx[i], ay + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if land[nx][ny] == 0 or land[nx][ny] > 1:
                continue
            land[nx][ny] = mark
            q.append((nx, ny))


def solution(land):
    mark = 2
    for i, row in enumerate(land):
        for j, item in enumerate(row):
            if item == 1:
                land[i][j] = mark
                bfs(i, j, land, mark)
                mark += 1
    answer = find_max(land)

    return answer