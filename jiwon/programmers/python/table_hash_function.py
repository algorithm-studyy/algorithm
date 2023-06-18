from functools import reduce


def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    result = []
    for i in range(row_begin - 1, row_end):
        result.append(sum([item % (i + 1) for item in data[i]]))

    return reduce(lambda answer, current: answer ^ current, result)
