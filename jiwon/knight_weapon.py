from math import sqrt


def solution(number, limit, power):
    answer = 0
    for num in range(1, number + 1):
        sqrt_num = int(sqrt(num))
        count = 0
        for n in range(1, sqrt_num + 1):
            if num == n * n:
                count += 1
            elif num % n == 0:
                count += 2
        answer += count if count <= limit else power
    return answer
