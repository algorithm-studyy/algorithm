import heapq


def dijkstra(start):
    distance = [int(1e9)] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


if __name__ == "__main__":
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    result = 0

    for _ in range(m):
        start, end, t = map(int, input().split())
        graph[start].append((end, t))

    for i in range(1, n + 1):
        go = dijkstra(i)
        back = dijkstra(x)
        result = max(result, go[x] + back[i])

    print(result)