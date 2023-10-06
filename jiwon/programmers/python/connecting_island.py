# n개의 섬 costs
# 다리를 여러 번 건너도 도달할 수만 있으면 통행 가능
from heapq import heappush, heappop, heapify
from collections import defaultdict


def solution(n, costs):
    answer = 0
    g = defaultdict(list)
    for v1, v2, cost in costs:
        g[v1].append([cost, v1, v2])
        g[v2].append([cost, v2, v1])
    visit = set([0])
    heap = g[0]
    heapify(heap)
    while heap:
        distance, current, destination = heappop(heap)
        if destination in visit:
            continue
        visit.add(destination)
        answer += distance
        for edge in g[destination]:
            if edge[2] not in visit:
                heappush(heap, edge)

    return answer
