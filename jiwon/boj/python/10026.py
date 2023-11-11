# 적록색약 R == G
# 적록색약 X -> R, G, B

# 적록색약 보드를 하나 만든다.
# bfs를 두 개 돈다.
from sys import stdin
from collections import deque


def set_board_rb():
    result = []
    for row in board:
        result.append([])
        for item in row:
            if item == 'G':
                result[-1].append('R')
            else:
                result[-1].append(item)
    return result


def solution(b):
    v = [[False] * n for _ in range(n)]
    count = 0
    for i, row in enumerate(b):
        for j, item in enumerate(row):
            if not v[i][j]:
                count += 1
                v[i][j] = True
                bfs(i, j, v, item, b)
    result.append(str(count))


def bfs(x, y, v, s, b):
    q = deque([(x, y)])
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            nx, ny = ax + dx[i], ay + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or v[nx][ny] or b[nx][ny] != s:
                continue
            v[nx][ny] = True
            q.append((nx, ny))


if __name__ == '__main__':
    result = []
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    n = int(stdin.readline())
    board = [list(stdin.readline().strip()) for _ in range(n)]
    board_rb = set_board_rb()
    solution(board)
    solution(board_rb)
    print(' '.join(result))
