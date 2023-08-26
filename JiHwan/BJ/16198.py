def dfs(x, energy):
    if len(w) == 2:
        answer.append(energy)
        return

    for i in range(1, len(w) - 1):
        new_energy = energy + w[i - 1] * w[i + 1]
        ball = w.pop(i)
        dfs(x + 1, new_energy)
        w.insert(i, ball)


if __name__ == "__main__":
    n = int(input())
    w = list(map(int, input().split()))
    answer = []
    num = 1
    dfs(num, 0)
    print(max(answer))
