def solution():
    n = int(input())
    arr = [list(map(int, input().split(' '))) for _ in range(n)]
    dp = [0] * 76
    max_val = 0
    for i in range(n):
        max_val = max(max_val, dp[i - 1])
        if i + arr[i][0] <= n:
            dp[i + arr[i][0]] = max(arr[i][1] + dp[i], dp[i + arr[i][0]])
    print(max(dp))


solution()
