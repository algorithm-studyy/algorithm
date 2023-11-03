# 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사
# 왼쪽으로 발사, 처음 더 높은 곳에서 수신
#### 풀이
# length,
# stack.pop(), length - 1, poped.append()
# while stack[-1] >= poped[-1]:
# answer[poped.pop()[0]] = length
# else stack

from sys import stdin

n = int(stdin.readline())
stack = list(map(int, stdin.readline().split()))
pop = []
arr = ["0"] * n
while stack:
    num = stack.pop()
    n -= 1
    pop.append((num, n))
    while stack and pop and stack[-1] >= pop[-1][0]:
        arr[pop.pop()[1]] = str(n)
print(' '.join(arr))
