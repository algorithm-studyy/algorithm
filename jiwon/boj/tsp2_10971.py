from sys import stdin
from sys import maxsize

answer = maxsize


def dfs(a, start, s):
    global answer
    if len(a) == m:
        s += b[start][a[0]]
        answer = answer if answer < s or b[start][a[0]] == 0 else s
        return
    for end in range(m):
        if c[end] or (a and b[start][end] == 0) or s + b[start][end] > answer:
            continue
        c[end] = True
        a.append(end)
        if len(a) >= 2:
            dfs(a, end, s + b[start][end])
        else:
            dfs(a, end, s)
        c[end] = False
        a.pop()


def get_line_input():
    n = int(stdin.readline())
    board = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(n)]
    return n, board


if __name__ == '__main__':
    m, b = get_line_input()
    c = [False for _ in range(m)]
    dfs([], 0, 0)
    print(answer)
