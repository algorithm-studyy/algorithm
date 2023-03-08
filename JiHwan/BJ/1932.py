N = int(input())

dp = []

for i in range(N):
    num = list(map(int, input().split()))
    dp.append(num)

for i in range(1, N):
    for j in range(0, i + 1):
        if j==0:
            dp[i][0] += dp[i-1][0]
        elif i==j:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])


print(max(dp[N - 1]))
