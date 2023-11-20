# 1. 사이클이 아닌 녀석들
# 2.

from sys import stdin
from collections import deque


def bfs(x):
    global result
    visit = set()
    q = deque([(x, set())])
    while q:
        start, cnt = q.popleft()
        if len(cnt) > 0 and x == start:
            result = result.union(cnt)
            return
        start = students[start] - 1
        if start not in visit:
            cnt.add(start)
            q.append((start, cnt))
            visit.add(start)


if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        students = list(map(int, stdin.readline().split()))
        result = set()
        for i in range(n):
            if i not in result:
                bfs(i)
        print(n - len(result))
