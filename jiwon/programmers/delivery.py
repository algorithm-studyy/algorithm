from heapq import heappush, heappop


def change_graph(road, N):
    g = [dict() for _ in range(N + 1)]
    for a, b, k in road:
        g[a][b] = min(g[a][b], k) if g[a].get(b) else k
        g[b][a] = min(g[b][a], k) if g[b].get(a) else k
    return g


def dijikstra(start, g, K):
    d = [1e9 for _ in range(len(g))]
    d[start] = 0
    q = []
    heappush(q, [0, start])
    while q:
        distance, end = heappop(q)
        if distance > d[end]:
            continue
        for new_end, new_distance in g[end].items():
            another_distance = new_distance + distance
            if another_distance < d[new_end]:
                d[new_end] = another_distance
                heappush(q, [another_distance, new_end])
    return sum([1 for v in d if v <= K])


def solution(N, road, K):
    g = change_graph(road, N)
    return dijikstra(1, g, K)
