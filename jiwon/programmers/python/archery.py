answer = [0]


# 뒤부터 분배 모든 경우의 수.
def get_score_diff(lion, apeach):
    lion_score = 0
    apeach_score = 0
    for i, v in enumerate(lion):
        if lion[i] == 0 and apeach[i] == 0:
            continue
        if lion[i] > apeach[i]:
            lion_score += 10 - i
        else:
            apeach_score += 10 - i
    return lion_score - apeach_score


def is_get_more_lower_score(lion):
    for i in range(10, -1, -1):
        if lion[i] > answer[i]:
            return True
    return False


def dfs(d, lion, apeach, n, start):
    global answer
    if d == n:
        score = get_score_diff(lion, apeach)
        answer = lion + [score] if score > answer[-1] else answer
        answer = lion + [score] if score == answer[-1] and is_get_more_lower_score(lion) else answer
        return
    for i in range(start, 11):
        if lion[i] > apeach[i]:
            continue
        lion[i] += 1
        dfs(d + 1, lion, apeach, n, i)
        lion[i] -= 1


def solution(n, info):
    dfs(0, [0 for _ in range(11)], info, n, 0)
    return answer[:-1] if answer[-1] != 0 else [-1]
