def solution(topping):
    answer = 0

    for i in range(1, len(topping)):
        a = set(topping[i:])
        b = set(topping[:i])
        if len(a) == len(b):
            answer += 1

    return answer