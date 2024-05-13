def get_wall_board(n, arr):
    board = []
    for item in arr:
        num = 2 ** n
        row = ""
        for _ in range(n, -1, -1):
            if item >= num:
                item -= num
                row += "#"
            else:
                row += " "
            num //= 2
        board.append(row)
    return board


def solution(n, arr1, arr2):
    answer = []
    board1 = get_wall_board(n - 1, arr1)
    board2 = get_wall_board(n - 1, arr2)
    for i in range(n):
        row = ""
        for j in range(n):
            if board1[i][j] == "#" or board2[i][j] == "#":
                row += "#"
            else:
                row += " "
        answer.append(row)
    return answer