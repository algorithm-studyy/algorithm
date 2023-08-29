def dfs(x):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            if not visited[i]:
                board[x] == i

                if queen(x):
                    visited[i] = True
                    dfs(x + 1)
                    visited[i] = False


def queen(x):
    for i in range(n):
        if board[x] == board[i] or x - i == abs(board[x] - board[i]):
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    answer = 0
    board = [0] * n
    visited = [False] * n
    dfs(0)
    print(answer)
