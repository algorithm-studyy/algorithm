from math import sqrt, ceil


def solution(brown, yellow):
    answer = []
    start = int(ceil(sqrt(brown + yellow)))
    end = brown + yellow
    for i in range(start, end):
        if end % i != 0:
            continue
        j = end // i
        if (i - 2) * (j - 2) == yellow:
            answer = [i, j]
    return answer
