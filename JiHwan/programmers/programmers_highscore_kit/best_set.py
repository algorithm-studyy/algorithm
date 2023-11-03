def solution(n, s):
    answer = [0, 0]

    if n > s:
        return [-1]
    else:
        if s % n == 0:
            vector = s // n
            answer[0] = vector
            answer[1] = vector
        else:
            num = s // n

            answer[0] = num
            answer[1] = num + 1

    return answer