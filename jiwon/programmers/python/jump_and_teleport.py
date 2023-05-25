# k만큼 가거나, 현재까지 온 거리 x 2로 가거나
# k는 건전지 사용량이 k만큼 줄어듦

from collections import deque


def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
    return ans