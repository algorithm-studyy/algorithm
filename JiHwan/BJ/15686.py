import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
home = []
store = []
answer = 99999

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        if city[i][j] == 2:
            store.append([i, j])

for num in combinations(store, m):
    count = 0

    for h in home:
        tmp = 999
        for j in range(m):
            tmp = min(tmp, abs(h[0] - num[j][0]) + abs(h[1] - num[j][1]))
        count += tmp
    answer = min(answer, count)

print(answer)
