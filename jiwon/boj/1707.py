from sys import stdin
from collections import deque


def bfs(s):
    q = deque([s])
    visited[s] = 1
    while q:
        nv = q.popleft()
        for i in g[nv]:
            if visited[i] != 0 and visited[nv] != visited[i]:
                print(visited[nv], visited[i], nv, i)
                return False
            elif visited[i]:
                continue
            visited[i] = visited[nv] * -1
            q.append(i)
    return True


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        v, e = map(int, stdin.readline().split(' '))
        g = [[] for _ in range(v)]
        visited = [0] * v
        for _ in range(e):
            a, b = map(int, stdin.readline().split(' '))
            g[a - 1].append(b - 1)
            g[b - 1].append(a - 1)
        for a in range(v):
            if visited[a] == 0:
                tf = bfs(a)
                if not tf:
                    print('NO')
                    break
        else:
            print('YES')
        print(visited)

# 1
# 5 4
# 1 2
# 3 4
# 3 5
# 4 5