def solution(n):
    answer = []

    def dfs(d, start, end, via):
        if d == 1:
            answer.append([start, end])
            return
        dfs(d - 1, start, via, end)
        answer.append([start, end])
        dfs(d - 1, via, end, start)
    dfs(n, 1, 3, 2)
    return answer
