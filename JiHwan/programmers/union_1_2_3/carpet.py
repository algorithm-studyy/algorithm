def solution(brown, yellow):
    answer = []
    rec = brown + yellow
    small = 1000000001
    for i in range(1, rec // 2):
        if rec % i == 0:
            j = rec // i
            diff = abs(i - j)

            if diff <= small:
                small = diff
                result_i, result_j = i, j

    answer.append(result_i)
    answer.append(result_j)

    return sorted(answer, reverse=True)