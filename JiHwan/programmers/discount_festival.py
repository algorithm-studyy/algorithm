# 할인하는 제품은 하루에 하나씩만 구매 가능
# 회원가입하면 10일동안 회원 자격

from collections import Counter


def solution(want, number, discount):
    answer = 0
    total = {}
    for w, n in zip(want, number):
        total[w] = n

    for i in range(len(discount)):
        count = Counter(discount[i:i + 10])
        # print(dict(count))
        if count == total:
            answer += 1

    return answer