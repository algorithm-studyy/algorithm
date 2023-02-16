from sys import stdin


def solution():
    a = int(stdin.readline().strip())
    dp = [0] * (max(a + 1, 5))
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, a + 1):
        dp[i] = (dp[i - 1] % 10007 + dp[i - 2] % 10007) % 10007
    print(dp[a])


solution()
