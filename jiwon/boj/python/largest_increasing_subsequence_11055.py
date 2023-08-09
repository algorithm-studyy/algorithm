def solution():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    dp = []
    for i in range(n):
        dp.append(arr[i])
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(arr[i] + dp[j], arr[i], dp[i])
    print(max(dp))


solution()
