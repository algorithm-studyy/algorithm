from sys import stdin


def is_same_row(x, y):
    for i in range(9):
        if i == x:
            continue
        if b[y][x] == b[y][i]:
            return True
    return False


def is_same_column(x, y):
    for i in range(9):
        if i == y:
            continue
        if b[y][x] == b[i][x]:
            return True
    return False


def is_same_value_in_block(x, y):
    start_x, end_x = (x // 3) * 3, (x // 3 + 1) * 3
    start_y, end_y = (y // 3) * 3, (y // 3 + 1) * 3
    print(start_y, end_y, start_x, end_x, y, x)
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            if i == x and j == y:
                continue
            if b[i][j] == b[y][x]:
                return True
    return False


def find_zero():
    result = []
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                result.append((i, j))
    return result


def dfs(d):
    if d == n:
        for row in b:
            print(*row)
        exit(0)
    for idx in range(d, n):
        y, x = zeros[idx]
        for i in range(1, 10):
            b[y][x] = i
            if is_same_row(x, y) or is_same_column(x, y) or is_same_value_in_block(x, y):
                continue
            dfs(d + 1)
            b[y][x] = 0


b = [list(map(int, stdin.readline().split())) for _ in range(9)]
zeros = find_zero()
n = len(zeros)
print(n)
dfs(0)
