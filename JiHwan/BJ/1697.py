from collections import deque


def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        direction = [x - 1, x + 1, x * 2]
        if x == K:
            print(graph[x])
            break
        for nx in direction:
            if 0 <= nx <= max_size and not graph[nx]:
                graph[nx] = graph[x] + 1
                queue.append(nx)


if __name__ == "__main__":
    N, K = map(int, input().split())
    max_size = 100000
    graph = [0] * (max_size+1)
    bfs()

