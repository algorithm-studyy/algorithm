from collections import deque
from sys import stdin, maxsize

# 현재 필요한 것
# 1. 현재 이모티콘의 개수
# 2. 클립보드의 이모티콘
# 3. 시간(횟수)
# ax => 현재 이모티콘의 개수
# ay => 클립보드의 이모티콘
# v[ax][ay] => 시간 횟수


def bfs(x):
    q = deque([[x, 0]])
    v[x][0] = 0
    while q:
        ax, ay = q.popleft()
        if ax == n:
            return v[ax][ay]
        if 0 < ax <= n + 1 and 0 < ax + ay <= n + 1:
            # 1. 복사
            if v[ax][ay] + 1 < v[ax][ax]:
                v[ax][ax] = v[ax][ay] + 1
                q.append([ax, ax])
            # 2. 붙여넣기
            if v[ax][ay] + 1 < v[ax + ay][ay]:
                v[ax + ay][ay] = v[ax][ay] + 1
                q.append([ax + ay, ay])
            # 3. 삭제
            if v[ax][ay] + 1 < v[ax - 1][ay]:
                v[ax - 1][ay] = v[ax][ay] + 1
                q.append([ax - 1, ay])


if __name__ == '__main__':
    n = int(stdin.readline())
    v = [[maxsize] * 1002 for _ in range(1002)]
    print(bfs(1))

