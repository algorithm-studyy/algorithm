# 1. 최대 공약수 찾기
# 2부터 나누기 ... min()까지
# 1이 있으면 종료하고, 나눈 수 * 나머지 수

from math import gcd


def solution(arr):
    answer = arr[0]
    for i, v in enumerate(arr):
        answer = answer * v // gcd(v, answer)
    return answer
