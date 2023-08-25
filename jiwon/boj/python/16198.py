# N개의 에너지 구슬
# 1 2 3 4
# x = 3 -> w = 2 * 4
# 1 2 4
# x = 2 -> w += 1 * 4
from sys import stdin


def dfs(arr, val):
    global answer
    if len(arr) == 2:
        answer = max(answer, val)
        return
    for idx in range(1, len(arr) - 1):
        new_arr = arr.copy()
        new_arr.pop(idx)
        dfs(new_arr, val + arr[idx - 1] * arr[idx + 1])


n = int(stdin.readline())
ws = list(map(int, stdin.readline().split()))
answer = 0
dfs(ws, 0)
print(answer)
