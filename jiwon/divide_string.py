def solution(s):
    answer = 0
    x = ''
    x_cnt = 0
    x_not_cnt = 0
    for c in s:
        if x_cnt == x_not_cnt:
            x = c
            answer += 1
        if x == c:
            x_cnt += 1
        elif c != x:
            x_not_cnt += 1

    return answer
