# 헛간의 수 N
# 소등릐 길 M 양방향 길
# C 마리의 소
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))
    return distance[N]


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    INF = 1e8
    distance = [INF] * (N + 1)
    for _ in range(M):
        a, b, c = map(int, input().split())
        arr[a].append((b, c))
        arr[b].append((a, c))


    print(dijkstra(1))