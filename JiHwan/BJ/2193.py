n = int(input())

# def dp(i):
#     if i == 1:
#         return 1
#     if i == 2:
#         return 1
#     else:
#         return dp(i-1)+dp(i-2)
#
# if __name__ == "__main__":
#     for i in range(3, 91):
#         dp(n)
#     print(dp(n))

dp = [0, 1, 1]

for i in range(3, 91):
    answer = dp[i-1]+dp[i-2]
    dp.append(answer)
print(dp[n])