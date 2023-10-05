# n개의 섬 costs
# 다리를 여러 번 건너도 도달할 수만 있으면 통행 가능
from heapq import heappush, heappop


def solution(n, costs):
    g = {k:dict() for k in range(n)}
    for v1, v2, cost in costs:
        g[v1][v2] = cost
        g[v2][v1] = cost
    d = [float('inf')] * n
    heap = []
    heappush(heap, (0, 0))
    d[0] = 0
    while heap:
        distance, current  = heappop(heap)
        if d[current] < distance:
            continue
        for e in g[current]:
            nd = g[current][e]
            if nd < d[e]:
                d[e] = nd
                heappush(heap, (nd, e))
    return sum(d)