n, m = map(int, input().split())
arr = list(map(int, input().split()))
set_arr = list(set(arr))
set_arr.sort()
stack = []


def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(len(set_arr)):
        if set_arr[i] not in stack:
            stack.append(set_arr[i])
            dfs()
            stack.pop()


dfs()