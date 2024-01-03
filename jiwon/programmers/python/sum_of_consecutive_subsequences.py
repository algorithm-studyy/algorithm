def solution(sequence, k):
    answer_list = []
    start = 0
    end = 0
    num = sequence[0]
    pre = 0
    while pre != num:
        pre = num
        if k == num:
            answer_list.append([start, end])

        if k <= num:
            num -= sequence[start]
            start += 1
        elif k > num:
            end += 1
            if end < len(sequence):
                num += sequence[end]

    answer_list.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer_list[0]
