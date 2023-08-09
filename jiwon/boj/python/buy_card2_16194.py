from sys import stdin


def solution():
    n = int(stdin.readline().strip())
    p = list(map(int, stdin.readline().strip().split(" ")))
    dp = p.copy()
    for i in range(n):
        for j in range(1, i + 1):
            dp[i] = min(dp[i], dp[i - j] + p[j - 1])
    print(dp[n - 1])


solution()
