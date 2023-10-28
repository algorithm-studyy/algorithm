# 2, 3번 연산의 최솟값
# index로 위치 찾고 right, left


from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
dq = deque([i for i in range(1, n + 1)])
answer, pop, right = 0, 0, n
while pop < m:
    target = dq.index(arr[pop])
    if right - target > target:
        answer += target
        dq.rotate(-target)
    else:
        answer += right - target
        dq.rotate(right - target)
    dq.popleft()
    pop += 1
    right -= 1
print(answer)
