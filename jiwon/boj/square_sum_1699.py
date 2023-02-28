from math import sqrt
from sys import maxsize


def solution():
    n = int(input())
    dp = [maxsize] * (n + 1)
    for i in range(1, n + 1):
        val = int(sqrt(i))
        if val ** 2 == i:
            dp[i] = 1
            continue
        for j in range(1, val + 1):
            dp[i] = min(dp[i - j ** 2] + dp[j ** 2], dp[i])
    print(dp[n])


solution()
