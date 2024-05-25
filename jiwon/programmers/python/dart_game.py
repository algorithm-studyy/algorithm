from collections import deque


def get_score(dart):
    result = ""
    while dart and dart[0].isdigit():
        result += dart.popleft()
    return int(result)


def processing_option(dart, score, scores):
    if dart and dart[0] == '*':
        score *= 2
        if scores:
            scores[len(scores) - 1] *= 2
        dart.popleft()
    elif dart and dart[0] == '#':
        score *= - 1
        dart.popleft()
    scores.append(score)


def solution(dartResult):
    bonus_dict = {k: i for i, k in enumerate(['S', 'D', 'T'], start=1)}
    dart = deque(dartResult)
    scores = []
    while dart:
        score = get_score(dart)
        bonus = dart.popleft()
        score = score ** bonus_dict[bonus]
        processing_option(dart, score, scores)
    return sum(scores)


print(solution("1S2D*3T"))
