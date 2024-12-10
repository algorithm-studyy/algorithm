n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []


def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    for i in arr:
        stack.append(i)
        dfs()
        stack.pop()


dfs()
