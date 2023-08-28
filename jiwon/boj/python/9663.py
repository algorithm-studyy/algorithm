n = int(input())
answer = 0
board = [0] * n


def is_queen(limit):
    for i in range(limit):
        if board[limit] == board[i] or limit - i == abs(board[i] - board[limit]):
            return False
    return True


def dfs(d):
    global answer
    if d == n:
        answer += 1
        return
    for i in range(n):
        board[d] = i
        if is_queen(d):
            dfs(d + 1)


dfs(0)
print(answer)
