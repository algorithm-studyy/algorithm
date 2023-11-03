from sys import stdin


def get_acc_sum_arr(n):
    arr = [[0] * (n + 1)]
    for _ in range(n):
        arr.append([0] + list(map(int, stdin.readline().split())))
    for i in range(1, n + 1):
        arr[1][i] += arr[1][i - 1]
        arr[i][1] += arr[i - 1][1]

    for i in range(2, n + 1):
        for j in range(2, n + 1):
            arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]
    return arr


def solution():
    n, m = map(int, stdin.readline().split())
    arr = get_acc_sum_arr(n)
    for _ in range(m):
        start_x, start_y, end_x, end_y = map(int, stdin.readline().split())
        answer = arr[end_x][end_y] - arr[start_x - 1][end_y] - arr[end_x][start_y - 1] + arr[start_x - 1][start_y - 1]
        print(answer)


solution()
