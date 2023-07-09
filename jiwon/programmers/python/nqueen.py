answer = 0


def check(d, v, row):
    for i in range(d):
        if row[i] == v or abs(v - row[i]) == d - i:
            return False
    return True


def dfs(d, n, row):
    global answer
    if d == n:
        answer += 1
        return
    for i in range(n):
        if check(d, i, row):
            row[d] = i
            dfs(d + 1, n, row)


def solution(n):
    dfs(0, n, [0] * n)
    return answer
