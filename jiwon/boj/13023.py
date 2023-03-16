from sys import stdin


def dfs(d, s):
    if d >= 5:
        print(1)
        exit()
    for i in g[s]:
        if not v[i]:
            v[i] = True
            dfs(d + 1, i)
            v[i] = False


if __name__ == '__main__':
    n, m = map(int, stdin.readline().split(' '))
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split(' '))
        g[a].append(b)
        g[b].append(a)
    v = [False] * n
    for j in range(n):
        v[j] = True
        dfs(1, j)
        v[j] = False
    print(0)
