def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * n
    for i, v in enumerate(arr):
        for j in range(i):
            if v > arr[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    print(max(dp))
    print(dp)


solution()
