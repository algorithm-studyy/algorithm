from sys import stdin, maxsize


def solution():
    n, m = map(int, stdin.readline().split())
    fuels = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
    dp = [[[maxsize] * 3 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        dp[0][i][0] = dp[0][i][1] = dp[0][i][2] = fuels[0][i]
    for i in range(1, n):
        for j in range(m):
            if j != 0:
                dp[i][j][2] = fuels[i][j] + min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1])
            if j != m - 1:
                dp[i][j][0] = fuels[i][j] + min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2])
            dp[i][j][1] = fuels[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])
    min_val = maxsize
    for j in range(m):
        min_val = min(min_val, min(dp[-1][j]))
    print(min_val)


solution()
