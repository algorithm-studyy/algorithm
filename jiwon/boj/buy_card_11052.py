from sys import stdin


def solution():
    n = int(stdin.readline().strip())
    p = list(map(int, stdin.readline().strip().split(" ")))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + p[j - 1])
    print(dp[n])


solution()
