from sys import maxsize


def solution():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    dp = [-maxsize] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + arr[i - 1] if dp[i - 1] > 0 else arr[i - 1]
    print(max(dp))


solution()
