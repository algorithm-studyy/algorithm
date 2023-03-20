import sys

N, M = map(int, sys.stdin.readline().split(" "))
relations = [[] for _ in range(N)]
visited = [False] * 2001

for i in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    relations[a].append(b)
    relations[b].append(a)


def dfs(x, depth):
    visited[x] = True
    if depth == 4:
        print(1)
        exit()
    for i in relations[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False


for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
