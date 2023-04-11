import sys
from collections import deque


def bfs(n):
    queue = deque()
    queue.append((1, 0))
    graph[1][0] = 1
    while queue:
        s, c = queue.popleft()
        if graph[s][s] == 0:
            graph[s][s] = graph[s][c] + 1
            queue.append((s, s))
        if s+c <= n and graph[s+c][c] == 0:
            graph[s+c][c] = graph[s][s] + 1
            queue.append((s+c, c))
        if 












if __name__ == "__main__":
    S = int(sys.stdin.readline())
    graph = [[0] * (S+1) for _ in range(S+1)]
    bfs(S)
