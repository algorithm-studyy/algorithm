from sys import stdin


def solution():
    n = int(stdin.readline())
    nums = [int(stdin.readline()) for _ in range(n)]
    max_num = max(nums)
    dp = [0] * max(3, max_num)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, max_num):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1_000_000_009
    for num in nums:
        print(dp[num - 1])


solution()
