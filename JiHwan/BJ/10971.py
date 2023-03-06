import sys


def dfs(start,move):
    global answer
    if start ==n:
        if  a[start][move]:
            value += a[start][move]
            if answer > value:
                answer = value
        return
    for i in range(n):
        if not visited[i] and a[start][i]:
            visited[i]=True
            dfs(start+1, move)
            visited[i]=False



n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [False]* n
answer = sys.maxsize
dfs(0,0)
print(answer)
