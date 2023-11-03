from collections import Counter


def solution(topping):
    answer = 0
    bro = Counter(topping)
    a = set()

    for i in topping:
        bro[i] -= 1
        if bro[i] == 0:
            bro.pop(i)
        a.add(i)
        if len(bro) == len(a):
            answer += 1
    return answer