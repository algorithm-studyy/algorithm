def solution(m, n, puddles):
    answer = 0
    board = [[0] * (m + 1) for _ in range(n + 1)]
    board[1][1] = 1

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                board[i][j] = 0
            else:
                board[i][j] = (board[i - 1][j] + board[i][j - 1]) % 1000000007

    return board[n][m]

    return answer