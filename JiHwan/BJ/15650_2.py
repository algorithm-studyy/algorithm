n, m = map(int, input().split())
arr = []


def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))

    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            print("백트래킹 전:", arr)
            dfs()
            arr.pop()
            print("백트래킹 후:", arr)


dfs()