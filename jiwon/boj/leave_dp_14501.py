def solution():
    n = int(input())
    arr = [list(map(int, input().split(' '))) for _ in range(n)]
    dp = [0] * 76
    for i in range(n):
        dp[i] = dp[i - 1] if dp[i - 1] != 0 and dp[i - 1] > dp[i] else dp[i]
        if i + arr[i][0] <= n:
            dp[i + arr[i][0]] = max(arr[i][1] + dp[i], dp[i + arr[i][0]])
    print(max(dp))


solution()
