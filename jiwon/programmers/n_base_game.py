# 진법 변환
# 순서에 맞게 주기
# 1. 모든 수를 진법변환해서 띄운 만큼 준다.
from string import ascii_uppercase


def change_base(i, dic, n):
    res = ''
    if i == 0:
        return '0'
    while i >= 1:
        i, r = divmod(i, n)
        if r >= 10:
            res += dic[r]
        else:
            res += str(r)
    return res[::-1]


def solution(n, t, m, p):
    answer = ''
    dic = {i:c for i, c in enumerate(ascii_uppercase, start=10)}
    base = ''
    for i in range(t * m):
        base += change_base(i, dic, n)
    for i in range(p - 1, t * m, m):
        answer += base[i]
    return answer
