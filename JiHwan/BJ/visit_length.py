def solution(dirs):
    x = 0
    y = 0
    result = set()
    direction = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    for d in dirs:
        dx, dy = direction[d]
        nx = x + dx
        ny = y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            result.add(((x, y), (nx, ny)))
            result.add(((nx, ny), (x, y)))
            x = nx
            y = ny
        # print(result)
    return len(result) // 2