
def dfs(num):
    if num == 10:
        return
    for i in range(1, 10):


if __name__ == "__main__" :
    board =[]
    for i in range(9):
        board.append(list(map(int, input())))
        for num in board:
            if num == 0:
                dfs(0)
    print(board)
