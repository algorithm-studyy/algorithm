from sys import stdin


def dfs(a, b):
    if a in b.keys():
        return b[a]

    if a % 2 == 0 and a % 3 == 0:
        b[a] = min(dfs(a // 2, b), dfs(a // 3, b)) + 1
    elif a % 3 == 0:
        b[a] = min(dfs(a // 3, b), dfs(a - 1, b)) + 1
    elif a % 2 == 0:
        b[a] = min(dfs(a // 2, b), dfs(a - 1, b)) + 1
    else:
        b[a] = dfs(a - 1, b) + 1

    return b[a]


if __name__ == '__main__':
    n = int(stdin.readline().strip())
    arr = {1: 0, 2: 1, 3: 1}
    dfs(n, arr)
    print(arr[n])

