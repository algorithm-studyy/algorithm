N = int(input())

t = []
p = []
dp = []

for i in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)
    dp.append(0)
dp.append(0)
for i in range(N-1, -1, -1):
    if t[i]+i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])

print(dp[0])
