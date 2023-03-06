import sys


def dfs(depth, key):
    global gap
    for i in range(0, n+1):
        if i not in start:
            link.append(i)
            power_1 = arr[start[i+1]][i+1] + arr[i+1][start[i+1]]
            power_2 = arr[link[i]][i+1] + arr[i+1][link[i+1]]
            gap = power_1 - power_2
            answer.append(gap)

    for i in range(n):
        start.append(i)
        dfs(depth + 1, key + 1)
        start.pop()


if __name__ == "__main__":
    n = int(input())
    start = []
    link = []
    answer = []
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dfs(0, 0)
    answer.sort()
    print(answer[0])
