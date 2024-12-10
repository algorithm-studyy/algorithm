# 각각의 상담을 완료하는데 걸리는 시간 T -> 금액 P

if __name__ == "__main__":
    N = int(input())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        T, P = map(int, input().split())
        if i + T - 1 < N + 1:
            dp[i + T - 1] = max(dp[i - 1] + P, dp[i + T - 1])
        dp[i] = max(dp[i - 1], dp[i])
    print(dp[-1])
