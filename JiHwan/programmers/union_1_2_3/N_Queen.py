def solution(n):
    answer = 0
    for i in range(n):
        answer += search(n, [i])

    return answer


def search(n, board):

    if len(board) == n:
        return 1
    count = 0
    for i in range(n):
        right = True
        for j in range(len(board)):
            if board[j] == i:
                right = False