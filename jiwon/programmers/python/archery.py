from collections import defaultdict
lions = defaultdict(list)


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


def dfs(d, lion, apeach, n, start):
    global lions
    if d == n:
        score = get_score_diff(lion, apeach)
        if score > 0:
            lions[score].append(lion.copy())
        return
    for i in range(start, 11):
        if lion[i] > apeach[i]:
            continue
        lion[i] += 1
        dfs(d + 1, lion, apeach, n, i)
        lion[i] -= 1


def solution(n, info):
    dfs(0, [0 for _ in range(11)], info, n, 0)
    if not lions:
        return [-1]
    answer = lions[max(lions.keys())]
    answer = sorted(answer, key=lambda x: tuple(x[i] for i in range(10, -1, -1)), reverse=True)[0]
    return answer
