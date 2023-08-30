from sys import stdin


def find_zero():
    result = 0
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                result += 1
    return result


def dfs(d):
    if d == n:
        for row in b:
            print(*row)


b = [list(map(int, stdin.readline().split())) for _ in range(9)]
n = find_zero()
