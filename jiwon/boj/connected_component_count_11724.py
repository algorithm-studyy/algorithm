from sys import stdin
from collections import deque


def bfs(v):
    visit[v] = True
    q = deque([v])
    while q:
        val = q.popleft()
        for j in g[val]:
            if not visit[j]:
                visit[j] = True
                q.append(j)


if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    answer = 0
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split(' '))
        g[a].append(b)
        g[b].append(a)

    visit = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visit[i]:
            answer += 1
            bfs(i)
    print(answer)


