# 1. 진수 바꾸기
# 2. 0p0, p0, 0p, p 패턴 체크하기
from math import sqrt


def change_base(n, k):
    a = ''
    while n >= 1:
        a += str(n % k)
        n = n // k
    return a[::-1]


def is_prime(value):
    if value < 2:
        return False
    for i in range(2, int(sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    nk = change_base(n, k)
    for i in nk.split('0'):
        answer = answer + 1 if i and is_prime(int(i)) else answer
    return answer
