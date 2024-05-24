import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    for i in range(n):
        for j in range(n):
            if i == n - 1 and j == n - 1:
                print(visited[i][j])
                break
            if i + arr[i][j] < n:
                visited[i + arr[i][j]][j] += visited[i][j]
            if j + arr[i][j] < n:
                visited[i][j + arr[i][j]] += visited[i][j]


