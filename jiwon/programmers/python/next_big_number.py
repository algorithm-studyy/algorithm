# 1. for문 반복
# 2. 이진수 변경
# 3. 1의 개수가 같은지 확인
from collections import Counter


def is_same_count_one(a, n):
    counter_a = Counter(bin(a))
    counter_n = Counter(bin(n))
    return counter_a['1'] == counter_n['1']


def solution(n):
    a = n + 1
    while not is_same_count_one(a, n):
        a += 1
    return a
