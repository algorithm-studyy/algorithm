from sys import stdin


def dfs(d, v):
    global max_answer, min_answer
    if d == n:
        max_answer, min_answer = max(max_answer, v), min(min_answer, v)
        return
    for i in range(4):
        if op_cnt[i] > 0:
            op_cnt[i] -= 1
            dfs(d + 1, cals[i](v, arr[d]))
            op_cnt[i] += 1


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
op_cnt = list(map(int, stdin.readline().split()))
cals = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x // y if x > 0 else -int(-x // y)]
max_answer, min_answer = -float('inf'), float('inf')
dfs(1, arr[0])
print(max_answer)
print(min_answer)
