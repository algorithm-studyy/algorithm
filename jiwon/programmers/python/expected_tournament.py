def solution(n,a,b):
    answer = 1

    s, e = min(a, b), max(a, b)
    while s % 2 == 0 or s + 1 != e:
        s = (s + 1) // 2
        e = (e + 1) // 2
        answer += 1
    return answer
