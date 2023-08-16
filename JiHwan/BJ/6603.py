def dfs(depth, start):
    global answer
    if depth == 6:
        print(' '.join(map(str, answer)))
    for i in range(start, len(n)):
        answer.append(n[i])
        dfs(depth + 1, i+1)
        answer.pop()


if __name__ == "__main__":
    answer = []
    while True:
        n = list(map(int, input().split()))
        if n[0] == 0:
            break
        del n[0]
        dfs(0, 0)
        print()
