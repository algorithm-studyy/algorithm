# u, d, l, r
dic = {k: i for i, k in enumerate('UDLR')}
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solution(dirs):
    x, y = 0, 0
    v = dict()
    for d in dirs:
        nx, ny = dx[dic[d]] + x, dy[dic[d]] + y
        if nx < -5 or nx > 5 or ny > 5 or ny < -5:
            continue
        route1 = ''.join(map(str, [x, y, nx, ny]))
        route2 = ''.join(map(str, [nx, ny, x, y]))
        x, y = nx, ny
        v[route1] = True
        v[route2] = True
    return len(v) // 2
