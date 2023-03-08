from sys import maxsize


def solution():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    dp = [-maxsize] * n
    sub = None
    dp[0] = arr[0]
    for i in range(1, n):
        if arr[i] < 0:
            if not sub:
                dp[i] = dp[i - 1]
                sub = arr[i]
                continue
            if sub > arr[i]:
                dp[i] = dp[i - 1] + sub
                sub = arr[i]
            else:
                dp[i] = dp[i - 1] + arr[i]
        else:
            dp[i] = dp[i - 1] + arr[i] if dp[i - 1] > 0 else arr[i]
    print(max(dp))
    print(dp)


solution()
