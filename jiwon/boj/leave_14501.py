from sys import stdin
from collections import Counter

answer = 0


def dfs(a, s):
    global answer
    if a >= n:
        answer = s if answer < s and a == n else answer
        return
    answer = s if answer < s else answer
    for i in range(a, n):
        dfs(i + tp[i][0], tp[i][1] + s)


if __name__ == '__main__':
    n = int(stdin.readline())
    tp = [list(map(int, stdin.readline().strip().split(" "))) for _ in range(n)]
    dfs(0, 0)
    print(answer)
