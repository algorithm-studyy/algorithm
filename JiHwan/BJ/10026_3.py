import sys

input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]


if __name__ == "__main__":
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * n for _ in range(n)]
    three_count
    for i in range(n):
        for j in range(n):
            bfs(i, j)
