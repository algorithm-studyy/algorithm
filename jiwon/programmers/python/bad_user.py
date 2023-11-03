# banned_id가 d
n = 0
answer = set()


def get_visit(visit):
    result = ''
    for i, v in enumerate(visit):
        if v:
            result += str(i)
    return result


def is_same(ui, bi):
    for u, b in zip(ui, bi):
        if b == '*':
            continue
        if u != b:
            return False
    return True


def dfs(d, user_id, banned_id, visit):
    global answer
    if d == n:
        answer.add(get_visit(visit))
        return
    bi = banned_id[d]
    for i, ui in enumerate(user_id):
        if len(bi) != len(ui) or visit[i]:
            continue
        if is_same(ui, bi):
            visit[i] = True
            dfs(d + 1, user_id, banned_id, visit)
            visit[i] = False


def solution(user_id, banned_id):
    global n
    n = len(banned_id)
    dfs(0, user_id, banned_id, [False] * len(user_id))
    return len(answer)