def solution(park, routes):
    answer = []

    x, y = 0, 0

    op = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j

    for i in routes:
        dx, dy = op[i.split()[0]]
        n = int(i.split()[1])

        xx, yy = x, y
        can_move = True

        for _ in range(n):
            nx = xx + dx
            ny = yy + dy

            if 0 <= nx <= len(park) - 1 and 0 <= ny <= len(park[0]) - 1 and park[nx][ny] != 'X':
                can_move = True
                xx, yy = nx, ny
            else:
                can_move = False
                break
        if can_move:
            x, y = nx, ny
    return [x, y]