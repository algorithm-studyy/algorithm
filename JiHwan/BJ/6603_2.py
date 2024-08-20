stack = []


def dfs(start):
    if len(stack) == 6:
        print(' '.join(map(str, stack)))

    for i in range(start, len(arr)):
        if arr[i] not in stack:
            stack.append(arr[i])
            dfs(i + 1)
            stack.pop()


if __name__ == "__main__":
    while True:
        arr = list(map(int, input().split()))
        if arr[0] == 0:
            break
        dfs(1)
        print()
