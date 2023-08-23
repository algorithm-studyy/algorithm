def solution(board):
    n = len(board)
    m = len(board[0])
    temp = []

    answer = 1

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] += min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1])

    for i in range(1, len(board)):
        temp.append(max(board[i]))
        answer = max(temp)
    return answer ** 2