n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []


def dfs(start):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
    for i in range(start, len(arr)):
        if arr[i] not in stack:
            stack.append(arr[i])
            dfs(i + 1)
            stack.pop()


dfs(0)
