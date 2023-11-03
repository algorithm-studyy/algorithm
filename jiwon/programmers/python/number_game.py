from bisect import bisect_right


def solution(A, B):
    B.sort()
    answer = 0
    for a_num in A:
        i = bisect_right(B, a_num)
        if i == len(B):
            continue
        elif B[i] > a_num:
            answer += 1
            B.pop(i)
    return answer
