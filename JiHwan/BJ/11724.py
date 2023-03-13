import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
graph = [[False] for _ in range(N+1)]\

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

