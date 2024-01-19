from collections import deque


def bfs(x, y, color):
    queue = deque()
    queue.append((x, y))


if __name__ == "__main__":
    arr = [list(input()) for _ in range(12)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    result = 0

    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                count += bfs(i, j, arr[i][j])

    if count == 0:
        print(count)
    else:
        result += 1

