n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []


def dfs(start):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    for i in range(start, len(arr)):
        stack.append(arr[i])
        dfs(i)
        stack.pop()


dfs(0)
