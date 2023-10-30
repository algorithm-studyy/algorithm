from collections import deque


def get_graph(edge, n):
    g = {i + 1: [] for i in range(n)}
    for s, e in edge:
        g[s].append(e)
        g[e].append(s)
    return g


def solution(n, edge):
    answer = 0
    route = [0] * (n + 1)
    g = get_graph(edge, n)
    q = deque([1])
    while q:
        s = q.popleft()
        for e in g[s]:
            if route[e] != 0 or e == 1:
                continue
            route[e] = route[s] + 1
            q.append(e)
    return route.count(max(route))
