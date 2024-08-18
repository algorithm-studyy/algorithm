n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []


def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
    for i in arr:
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()


dfs()