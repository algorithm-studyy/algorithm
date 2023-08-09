from sys import stdin
from collections import deque


def dfs(d):
    for i in g[d]:
        if not visit[i]:
            answer[0].append(i)
            visit[i] = True
            dfs(i)


def bfs(d):
    q = deque([d])
    while q:
        val = q.popleft()
        for i in g[val]:
            if not visit[i]:
                answer[1].append(i)
                visit[i] = True
                q.append(i)


if __name__ == '__main__':
    n, m, v = map(int, input().split(' '))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split(' '))
        g[a].append(b)
        g[b].append(a)
        g[a].sort()
        g[b].sort()
    visit = [False] * (n + 1)
    visit[v] = True
    answer = [[str(v)], [str(v)]]
    dfs(v)
    visit = [False] * (n + 1)
    visit[v] = True
    bfs(v)
    print(*answer[0])
    print(*answer[1])
