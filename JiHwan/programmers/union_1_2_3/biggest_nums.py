import itertools


def solution(numbers):
    answer = ''
    npr = itertools.permutations(numbers, len(numbers))
    list_npr = []

    list_npr = max(''.join(map(str, i)) for i in npr)

    return list_npr