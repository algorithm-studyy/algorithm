
def solution(x, y, n):
    dp = dict()
    dp[x] = 0
    while y > x:
        x3, x2, xn = x * 3, x * 2, x + n
        dp[x3] = dp[x] + 1 if x3 not in dp else min(dp[x] + 1, dp[x3])
        dp[x2] = dp[x] + 1 if x2 not in dp else min(dp[x] + 1, dp[x2])
        dp[xn] = dp[x] + 1 if xn not in dp else min(dp[x] + 1, dp[xn])
        x += 1
        while x not in dp:
            x += 1
    return dp[y] if y in dp else -1
