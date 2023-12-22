import sys


def check(x, y, z):
    global white, blue
    color = board[x][y]
    for i in range(x, x + z):
        for j in range(y, y + z):
            if color != board[i][j]:
                check(x, y, z // 2)
                check(x, y + z // 2, z // 2)
                check(x + z // 2, y, z // 2)
                check(x + z // 2, y + z//2, z // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    white = 0
    blue = 0
    check(0, 0, n)
    print(white)
    print(blue)
