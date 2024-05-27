from collections import deque


def bfs(x, y):
    q = deque([(x, y)])
    init_value = board[x][y]
    v[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if nx < 0 or nx >= a or ny < 0 or ny >= b or v[nx][ny] or board[nx][ny] != init_value:
                continue
            v[nx][ny] = True
            count += 1
            q.append((nx, ny))
    return count


b, a = map(int, input().split())

board = []
for _ in range(a):
    board.append(input().strip())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
v = [[False] * b for _ in range(a)]

w_result = 0
b_result = 0
for i in range(a):
    for j in range(b):
        if not v[i][j]:
            cnt = bfs(i, j)
            if board[i][j] == 'W':
                w_result += cnt ** 2
            else:
                b_result += cnt ** 2
print(w_result, b_result)
