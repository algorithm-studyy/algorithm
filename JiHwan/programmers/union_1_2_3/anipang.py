def solution(m, n, board):
    answer = 0

    board = [list(row) for row in board]
    bang = set()

    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                icon = board[i][j]
                if icon == []:
                    continue
                elif board[i][j + 1] == icon and board[i + 1][j] == icon and board[i + 1][j + 1] == icon:
                    bang.add((i, j))
                    bang.add((i + 1, j))
                    bang.add((i, j + 1))
                    bang.add((i + 1, j + 1))

        if bang:
            answer += len(bang)
            for i, j in bang:
                board[i][j] = []
        else:
            return answer

        if board[i][j]

