def find_to_start(park):
    for i, row in enumerate(park):
        for j, item in enumerate(row):
            if item == 'S':
                return (i, j)
    return None


def is_blocked_x(y, s, e, park):
    for i in range(s, e + 1):
        if park[y][i] == 'X':
            return True
    return False


def is_blocked_y(x, s, e, park):
    for i in range(s, e + 1):
        if park[i][x] == 'X':
            return True
    return False


def solution(park, routes):
    go = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}
    y, x = find_to_start(park)
    for route in routes:
        direction, size = route.split(" ")
        dy, dx = go[direction]
        ny, nx = y + dy * int(size), x + dx * int(size)
        if ny < 0 or ny >= len(park) or nx < 0 or nx >= len(park[0]):
            continue
        if is_blocked_x(y, min(x, nx), max(x, nx), park) or is_blocked_y(x, min(y, ny), max(y, ny), park):
            continue
        x, y = nx, ny
    return [y, x]
