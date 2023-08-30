def check_row(n, x):
    for i in range(9):
        if n == board[x][i]:
            return False
    return True


def check_col(n, y):
    for i in range(9):
        if n == board[i][y]:
            return False
    return True


def three_box(n, x, y):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == board[nx][ny]:
                return False
    return True


def dfs(n):
    if n == len(blank):
        for i in range(9):
            for j in range(9):
                print(board[i][j])

    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]

        if check_col(i, y) and check_row(i, x) and three_box(i, x, y):
            board[x][y] = i
            dfs(x + 1)
            board[x][y] = 0


if __name__ == "__main__":
    board = []
    blank = []
    for i in range(9):
        board.append(list(map(int, input().split())))
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                blank.append((i, j))
    dfs(0)
