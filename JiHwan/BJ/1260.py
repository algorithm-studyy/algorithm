from collections import deque

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1


def dfs(matrix, i, visited):
    stack = [i]
    while stack:
        value = stack.pop()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True
        for c in range(len(matrix[value]) - 1, -1, -1):
            if matrix[value][c] == 1 and not visited[c]:
                stack.append(c)


dfs(matrix, v, visited)


def bfs(matrix, i, visited):
    queue = deque()
    queue.append(i)
    while queue:
        value = queue.popleft()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True
            for c in range(len(matrix[value])):
                if matrix[value][c] == 1 and not visited[c]:
                    queue.append(c)


bfs(matrix, v, visited)
