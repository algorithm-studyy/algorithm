# 1. 사이클이 아닌 녀석들
# 2.

from sys import stdin
from collections import deque


def bfs(x):
    global result, done
    q = deque([(x, 0)])
    while q:
        start, cnt = q.popleft()
        if cnt > 0 and x == start:
            result -= cnt
            return
        end = students[start] - 1
        if x != end == start:
            result -= 1
            return
        if end not in done:
            q.append((end, cnt + 1))
            done.add(end)
        else:
            return


if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        students = list(map(int, stdin.readline().split()))
        result = n
        done = set()
        for i in range(n):
            if i not in done:
                bfs(i)
        print(result)

