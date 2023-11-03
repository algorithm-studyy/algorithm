# 동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
# 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
# # 그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():

    while coin:
        x1, y1, x2, y2, count = coin.popleft()
        if count >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            nx2 = x2 + dx[i]
            ny1 = y1 + dy[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if matrix[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if matrix[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                coin.append((nx1, ny1, nx2, ny2, count + 1))

            elif 0 <= nx1 < n and 0 <= ny1 < m:
                return count + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:
                return count + 1
            else:
                continue
    return -1


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    matrix = [list(map(str, input().strip())) for _ in range(n)]
    coin = deque()

    temp = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "o":
                temp.append((i, j))
    coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))
    print(bfs())
