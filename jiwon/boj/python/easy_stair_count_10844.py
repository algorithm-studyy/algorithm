from sys import stdin


def solution():
    n = int(stdin.readline())
    dp = [[0] * 10 for _ in range(n + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, n + 1):
        dp[i][1] = dp[i - 1][0]
        dp[i][8] = dp[i - 1][9]
        for j in range(1, 9):
            dp[i][j - 1] += dp[i - 1][j]
            dp[i][j + 1] += dp[i - 1][j]
    print(sum(dp[n]) % 10_0000_0000)


solution()
