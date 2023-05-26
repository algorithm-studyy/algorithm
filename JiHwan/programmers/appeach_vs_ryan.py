from itertools import combinations_with_replacement


def solution(n, info):
    answer = []
    score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    ryan_score = list(combinations_with_replacement(score, n))
    num_ryan_score = []

    for case in ryan_score:
        s = [0 for _ in range(11)]
        for l in case:
            s[10 - l] += 1
        num_ryan_score.append(s)

    for case in num_ryan_score:
        s = [0 for _ in range(11)]
        bigger_than_appeach = []
        for i in range(11):
            if info[i] > 0 or case[i] > 0:
                if info[i] < case[i]:
                    s[10 - i] += 1
                elif info[i] > case[i]:

    return answer