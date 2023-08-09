from sys import stdin


def solution():
    n = int(input())
    rgb = [list(map(int, stdin.readline().split(' '))) for _ in range(n)]
    for i in range(1, n):
        for j in range(3):
            rgb[i][j] = min(rgb[i - 1][(j + 1) % 3], rgb[i - 1][(j + 2) % 3]) + rgb[i][j]

    print(min(rgb[n - 1]))


solution()
