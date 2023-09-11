# 네트워크 개수 ? 간선의 개수
# 간선의 개수를 어떻게 구할까
answer = dict()


def dfs(idf, cs, prev, v):
    global answer
    for i in range(len(cs[prev])):
        if cs[prev][i] == 0 or i == prev or i in v:
            continue
        v.add(i)
        answer[i] = idf
        dfs(idf, cs, i, v)


def solution(n, computers):
    global answer
    for i, c in enumerate(computers):
        if i not in answer:
            answer[i] = i
            dfs(i, computers, i, set())
    return len(set(answer.values()))
