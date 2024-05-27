'''
오른쪽, 아래쪽으로만 이동 가능
0이 종착점
방향은 변경 불가
'''

n = int(input())
b = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
     b.append(list(map(int, input().split())))


dp[0][0] = 1
for i in range(n):
    for j in range(n):
        nx = i - b[i][j]
        ny = j - b[i][j]
        if nx < 0:
            dp[i][j] = dp[i][ny]
        elif ny < 0:
            dp[i][j] = dp[nx][i]
        elif nx >= 0 and ny >= 0:
            dp[i][j] = dp[i][ny] + dp[nx][j]
for row in dp:
    print(*row)
print(dp[n - 1][n - 1])
