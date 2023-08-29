import sys


def dfs(col, row, depth, val):
    global answer
    if depth == 4:
        if val > answer:
            answer = total
        else:
            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        dfs(nr, nc, idx + 1, total + matrix[nr][nc])
                        visited[nr][nc] = False


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(int(n))]
    max_val = max(max(matrix))
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[False] * m for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, 1, matrix[i][j])
            visited[i][j] = False
