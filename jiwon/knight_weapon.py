
def get_divisor(num):
    n = 2
    pf = 1
    c = 0
    while num > 1:
        if num % n == 0:
            num //= n
            c += 1
        else:
            pf *= (c + 1)
            n += 1
            c = 0
    pf *= (c + 1)
    return pf


def solution(number, limit, power):
    answer = 1
    for i in range(2, number + 1):
        divisor = get_divisor(i)
        if divisor > limit:
            answer += power
        else:
            answer += divisor
    return answer