def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    def dfs(start, route):
        if len(route) == len(tickets) + 1:
            answer.append(route)
            return
        for i, ticket in enumerate(tickets):
            if not visited[i] and start == ticket[0]:
                visited[i] = True
                dfs(ticket[1], route + [ticket[1]])
                visited[i] = False

    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]
