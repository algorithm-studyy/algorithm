from sys import stdin


def solution():
    n = int(stdin.readline())
    t = [list(map(int, stdin.readline().split(' '))) for _ in range(n)]
    dp = [[0] * (i + 1) for i in range(n)]
    dp[0][0] = t[0][0]
    for i in range(n - 1):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + t[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + t[i + 1][j + 1])
    print(max(dp[n - 1]))


solution()
