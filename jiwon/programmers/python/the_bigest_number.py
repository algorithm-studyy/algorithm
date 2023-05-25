from functools import cmp_to_key


def cmp(a, b):
    ab, ba = a + b, b + a
    if ab > ba:
        return 1
    elif ab < ba:
        return -1
    return 0


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(cmp), reverse=True)
    return str(int(''.join(numbers)))
