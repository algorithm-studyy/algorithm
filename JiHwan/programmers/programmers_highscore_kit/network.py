def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(x):
        print(x)
        visited[x] = 1
        for key, value in enumerate(computers[x]):
            if value and visited[key] == 0:
                dfs(key)

    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    return answer