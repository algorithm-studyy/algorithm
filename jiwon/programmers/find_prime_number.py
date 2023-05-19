from math import sqrt
from itertools import permutations


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        for num in permutations(numbers, i):
            num = int(''.join(num))
            if is_prime(num):
                answer.add(num)
    return len(answer)
