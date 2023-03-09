from sys import maxsize


def solution():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    dp = [[-maxsize] * n for _ in range(2)]
    dp[0][0], dp[1][0] = arr[0], arr[0]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
        dp[1][i] = max(dp[1][i - 1] + arr[i], dp[0][i - 1])
    print(max(max(dp[1]), max(dp[0])))


solution()
