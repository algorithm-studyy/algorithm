from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    while q:
        dist = q.popleft()
        if dist == m:
            return visited[dist]
        for dx in (dist + 1, dist - 1, dist * 2):
            if 0 <= dx < MAX_NUM:
                if visited[dx] == 0:
                    if dx == dist * 2 and visited[dx] == 0:
                        visited[dx] = visited[dist]
                        q.append(dx)
                    else:
                        visited[dx] = visited[dist] + 1
                        q.append(dx)


if __name__ == "__main__":
    n, m = map(int, input().split())
    MAX_NUM = 100001
    visited = [0] * MAX_NUM
    print(bfs(n))

