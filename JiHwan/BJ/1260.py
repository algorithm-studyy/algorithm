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
        for k in range(len(matrix[value]) - 1, -1, -1):
            if matrix[value][k] == 1 and not visited[k]:
                stack.append(k)


dfs(matrix, v, visited)
print()
visited = [False] * (n + 1)


def bfs(matrix, i, visited):
    queue = deque()
    queue.append(i)
    while queue:
        value = queue.popleft()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True
            for k in range(len(matrix[value])):
                if matrix[value][k] == 1 and not visited[k]:
                    queue.append(k)


bfs(matrix, v, visited)
