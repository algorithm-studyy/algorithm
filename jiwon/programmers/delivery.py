route = set()


def change_graph(road, N):
    g = [dict() for _ in range(N + 1)]
    for a, b, k in road:
        g[a][b] = min(g[a][b], k) if g[a].get(b) else k
        g[b][a] = min(g[b][a], k) if g[b].get(a) else k
    return g


def dfs(d, s, g, K, v):
    global route
    if d > K:
        return
    route.add(s)
    for i in g[s].keys():
        if not v[i]:
            dfs(d + g[s][i], i, g, K, v)
            v[i] = True
        v[i] = False


def solution(N, road, K):
    global route
    g = change_graph(road, N)
    v = [False for _ in range(N + 1)]
    dfs(0, 1, g, K, v)
    return len(route)
