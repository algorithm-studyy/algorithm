import sys

N = int(sys.stdin.readline())

board = []
body = []

for _ in range(N):
    board.append(list(input().rstrip()))

for i in range(N):
    for j in range(N):
        if board[j][i] == '*':
            body.append((j, i))

body.sort()

heart = (body[0][0] + 1, body[0][1])
left = heart[1] - body[1][1]

print(left)
