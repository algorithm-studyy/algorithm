from sys import stdin


def get_line_input():
    n = int(stdin.readline())
    result = []
    max_val = 0
    for _ in range(n):
        num = int(stdin.readline().strip())
        max_val = max(num, max_val)
        result.append(num)
    return n, max_val, result


def solution():
    n, max_val, result = get_line_input()
    dp = [0] * (max_val + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, max_val + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    for i in result:
        print(dp[i])


solution()
