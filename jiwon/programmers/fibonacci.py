def solution(n):
    dp = [0, 1, 1, 2, 3, 5] + [0] * n
    for i in range(4, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
    return dp[n]