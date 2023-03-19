from sys import stdin
from collections import deque


def bfs(s):
    q = deque([s])
    visited[s] = True
    while q:
        nv = q.popleft()
        for i in g[nv]:
            if visited[i]:
                continue
            visited[i] = True
            q.append(i)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        v, e = map(int, stdin.readline().split(' '))
        g = [[] for _ in range(v)]
        visited = [False] * v
        for _ in range(e):
            a, b = map(int, stdin.readline().split(' '))
            g[a - 1].append(b - 1)
            # g[b - 1].append(a - 1)
        bfs(0)
        print(visited)
        if all(visited):
            print('NO')
        else:
            print('YES')


