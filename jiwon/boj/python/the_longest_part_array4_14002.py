def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[]] * n
    max_idx = 0
    max_val = 1
    for i, v in enumerate(arr):
        for j in range(i - 1, -1, -1):
            if v > arr[j]:
                if len(dp[j]) + 1 < len(dp[i]):
                    continue
                dp[i] = dp[j].copy()
                dp[i].append(v)
                if max_val <= len(dp[i]):
                    max_val = len(dp[i])
                    max_idx = i
        if not dp[i]:
            dp[i] = [arr[i]]
    print(max_val)
    print(' '.join(list(map(str, dp[max_idx]))))


solution()
