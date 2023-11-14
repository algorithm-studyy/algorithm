def bfs(x,y):
    x, y = queue.popleft()





if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    bfs(0, 0)



