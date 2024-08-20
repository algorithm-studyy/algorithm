def dfs(start):
    if len(stack) == l:
        vo, co = 0, 0
        for i in range(len(stack)):
            if stack[i] in consonant:
                co += 1
            else:
                vo += 1
        if co >= 1 and vo >= 2:
            print(''.join(map(str, stack)))
    for i in range(start, len(arr)):
        if arr[i] not in stack:
            stack.append(arr[i])
            dfs(i + 1)
            stack.pop()


if __name__ == "__main__":
    l, c = map(int, input().split())
    arr = sorted(list(map(str, input().split())))
    consonant = ['a', 'e', 'i', 'o', 'u']
    stack = []
    dfs(0)
