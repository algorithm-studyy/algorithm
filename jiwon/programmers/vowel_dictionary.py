words = list('AEIOU')
dic = dict()
cnt = 1


def dfs(d, lst):
    global dic, cnt
    if d >= 5:
        return
    for i, c in enumerate(words):
        lst.append(c)
        dic[''.join(lst)], cnt = cnt, cnt + 1
        dfs(d + 1, lst)
        lst.pop()


def solution(word):
    dfs(0, [])
    return dic[word]
