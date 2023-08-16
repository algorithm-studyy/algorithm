import sys


def dfs(value):
    global answer
    hap_1 = 0
    hap_2 = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if not visited[i] and visited[j]:
                    hap_1 = arr[i][j] + arr[j][i]
                else:
                    hap_2 = arr[i][j] + arr[j][i]
            else:
                continue
    answer = min(answer, abs(hap_1 - hap_2))

    for i in range(value, n):
        visited[i] = True
        dfs(value + 1)
        visited[i] = False


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(int(n))]
    visited = [False] * n
    answer = 1e9
    dfs(0)
    print(answer)
