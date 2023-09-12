def set_boarding(m, n, puddles):
    b = [[0] * m for _ in range(n)]
    for j, i in puddles:
        b[i - 1][j - 1] = -1
    b[n - 1][m - 1] = 1
    return b


def solution(m, n, puddles):
    b = set_boarding(m, n, puddles)
    dx = [1, 0]
    dy = [0, 1]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            for k in range(2):
                nx, ny = j + dx[k], i + dy[k]
                if 0 <= nx < m and 0 <= ny < n and b[i][j] != -1 and b[ny][nx] != -1:
                    b[i][j] = (b[i][j] + b[ny][nx]) % 1000000007

    return b[0][0]