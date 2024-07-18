n = int(input())
board = list(list(input().strip()) for _ in range(n))


def find_heart():
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == '*' and board[i + 1][j] == '*' and board[i - 1][j] == '*':
                return i, j


def find_start_legs(heart):
    for x in range(heart[0], n):
        if board[x][heart[1]] == '_':
            return {"L": (x - 1, heart[1] - 1), "R": (x - 1, heart[1] + 1)}


def cal_left_hand(heart):
    result = 0
    for y in range(heart[1] - 1, -1, -1):
        if board[heart[0]][y] == '_':
            return result
        result += 1
    return result


def cal_right_hand(heart):
    result = 0
    for y in range(heart[1] + 1, n):
        if board[heart[0]][y] == '_':
            return result
        result += 1
    return result


def cal_leg_and_heori(x, y):
    result = 0
    for i in range(x + 1, n):
        if board[i][y] == '_':
            return result
        result += 1
    return result


def solution():
    heart = find_heart()
    legs = find_start_legs(heart)
    answer = [cal_left_hand(heart),
              cal_right_hand(heart),
              cal_leg_and_heori(*heart),
              cal_leg_and_heori(*legs["L"]),
              cal_leg_and_heori(*legs["R"])
              ]
    print(heart[0] + 1, heart[1] + 1)
    print(*answer)


solution()

