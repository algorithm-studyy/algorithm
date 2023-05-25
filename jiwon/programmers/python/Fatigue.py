# 최소 피로도가 될 수 있는 것만 한다.
# 현재 남은 피로도 k < dungeons[i][0] k < dungeons[i][1]
answer = 0


def dfs(d, a, p, dungeons, visited):
    global answer
    if d >= len(dungeons):
        answer = max(a, answer)
        return
    for i, dungeon in enumerate(dungeons):
        if visited[i]:
            continue
        visited[i] = True
        if p < dungeon[0]:
            dfs(d + 1, a, p, dungeons, visited)
        else:
            dfs(d + 1, a + 1, p - dungeon[1], dungeons, visited)
        visited[i] = False


def solution(k, dungeons):
    dfs(0, 0, k, dungeons, [False] * len(dungeons))
    return answer
