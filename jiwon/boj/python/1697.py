from collections import deque
from sys import stdin


def bfs(s):
    q = deque([s])
    v[s] = 0
    while q:
        x = q.popleft()
        if x == k:
            return
        for i in a:
            nx = x * 2 if i == 2 else x + i
            if not v.get(nx) and 0 <= nx <= max_val + 1:
                v[nx] = v[x] + 1
                q.append(nx)


if __name__ == '__main__':
    n, k = map(int, stdin.readline().split(' '))
    max_val = max(n, k)
    a = [-1, 1, 2]
    v = {}
    bfs(n)
    print(v[k])
