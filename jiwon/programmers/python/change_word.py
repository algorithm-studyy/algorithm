answer = 1e9


def is_same_inner_value(a_list, b_list):
    for a, b in zip(a_list, b_list):
        if a != b:
            return False
    return True


def dfs(d, b, t, w, v):
    global answer
    if is_same_inner_value(b, t):
        answer = min(d, answer)
        return
    for word in w:
        for i in range(len(b)):
            if b[i] != word[i]:
                temp = b[i]
                b[i] = word[i]
                str_b = ''.join(b)
                if str_b in w and str_b not in v:
                    v.add(str_b)
                    dfs(d + 1, b, t, w, v)
                b[i] = temp


def solution(begin, target, words):
    if target not in words:
        return 0
    words.remove(target)
    words.insert(0, target)
    dfs(0, list(begin), list(target), words, set())
    return answer