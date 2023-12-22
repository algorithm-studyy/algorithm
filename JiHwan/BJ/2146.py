if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == 0:

