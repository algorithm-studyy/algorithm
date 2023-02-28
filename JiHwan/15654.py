n, m = map(int, input().split())

stack = []
arr = []

for i in range(n):
    k = input()
    arr.append(k)


def dfs(arr):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(1, n+1):
        stack.append(i)
        dfs(arr)
        stack.pop()


dfs(arr)