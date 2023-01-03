import re


def solution(babbling):
    answer = 0
    check = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for c in check:
            p = '(' + c + '){2,}'
            b = re.sub(p, '5', b)
            b = b.replace(c, ' ')
        if not b.strip():
            answer += 1
    return answer
