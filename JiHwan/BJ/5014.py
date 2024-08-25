# 총 높이 f
# 스타트 링크 위치 G
# 현재 위치 S
from collections import deque

f, s, g, u, d = map(int, input().split())
arr = [0 for _ in range(f + 1)]


def bfs():
    q = deque()
    q.append(s)

    arr[s] = 1

    while q:
        y = q.popleft()

        if y == g:
            return arr[y] - 1
        else:
            for x in (y + u, y - d):
                if (0 < x <= f) and arr[x] == 0:
                    arr[x] = arr[y] + 1
                    q.append(x)

    return "use the stairs"

print(bfs())

