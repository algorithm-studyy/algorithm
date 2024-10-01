import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in short[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))


if __name__ == "__main__":
    n, d = map(int, input().split())
    short = [[] for _ in range(d + 1)]
    distance = [int(1e9)] * (d + 1)

    for i in range(d):
        short[i].append((i + 1, 1))

    for _ in range(n):
        start, end, length = map(int, input().split())
        if end > d or end - start < length:
            continue
        short[start].append((end, length))

    dijkstra(0)
    print(distance[d])