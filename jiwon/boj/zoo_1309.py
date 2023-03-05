def solution():
    n = int(input())
    dp = [3, 7]
    for i in range(1, n):
        dp.append((dp[i - 1] + dp[i] * 2) % 9901)
    print(dp[n - 1])


solution()
