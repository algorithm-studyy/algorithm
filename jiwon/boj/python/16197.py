# 두 동전은 동시에 움직인다.
# 두 동전 중 하나만 떨어뜨려야 함
# 풀이 : 두 동전을 한 번에 움직이는 게 핵심
# count를 세서 10번 이상이면

from collections import deque
from sys import stdin

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def is_out(n, m, x, y):
    if y < 0 or y >= n or x < 0 or x >= m:
        return True
    return False


def find_coins(b, n, m):
    result = []
    for i in range(n):
        for j in range(m):
            if b[i][j] == 'o':
                result.append((i, j, 0))
    return deque(result)


def bfs(b, q, n, m, v1, v2):
    while q:
        y1, x1, cnt = q.popleft()
        y2, x2, _ = q.popleft()
        cnt += 1
        if cnt > 10:
            return -1
        for i in range(4):
            ny1, ny2, nx1, nx2 = y1 + dy[i], y2 + dy[i], x1 + dx[i], x2 + dx[i]
            out1, out2 = is_out(n, m, nx1, ny1), is_out(n, m, nx2, ny2)
            if out1 and out2:
                continue
            elif out1 or out2:
                return cnt
            if b[ny1][nx1] == '#' or v1[ny1][nx1] or b[ny2][nx2] == '#' or v2[ny2][nx2]:
                continue
            v1[ny1][nx1] = True
            v2[ny2][nx2] = True
            q.append((ny1, nx1, cnt))
            q.append((ny2, nx2, cnt))
            print(ny1, nx1, ny2, nx2, cnt, q)
    return -1


def solution():
    n, m = map(int, stdin.readline().split())
    b = [list(stdin.readline()) for _ in range(n)]
    v1 = [[False] * len(b[0]) for _ in range(len(b))]
    v2 = [[False] * len(b[0]) for _ in range(len(b))]
    coins = find_coins(b, n, m)
    v1[coins[0][0]][coins[0][1]] = True
    v2[coins[1][0]][coins[1][1]] = True

    print(bfs(b, coins, n, m, v1, v2))


solution()