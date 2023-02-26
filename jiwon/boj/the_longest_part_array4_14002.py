def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[]] * n
    max_idx = 0
    max_val = 0
    dp[0].append(arr[0])
    for i, v in enumerate(arr):
        for j in range(i - 1, -1, -1):
            if v > arr[j]:
                if len(dp[j]) + 1 < len(dp[i]):
                    continue
                dp[j].append(arr[i])
                dp[i] = dp[j].copy()
                if max_val < len(dp[i]):
                    max_val = len(dp[i])
                    max_idx = i
                break
            else:
                dp[i] = [arr[i]]
    print(len(dp[max_idx]))
    print(' '.join(list(map(str, dp[max_idx]))))


solution()
