import sys

answer=0
def dfs(num_list):
    global answer
    if len(num_list) == n:
        total = 0
        for i in range(n-1):
            total += abs(num_list[i]-num_list[i-1])

        answer = max(answer,total)
        return

    for i in range(n):
        if not visited[i]:
            visited[i]=True
            num_list.append(num[i])
            dfs(num_list)
            visited[i]=False
            num_list.pop()


if __name__ == '__main__':
    n = int(input())
    num = list(map(int, sys.stdin.readline().split()))
    visited = [False]*n

    dfs([])
    print(answer)
