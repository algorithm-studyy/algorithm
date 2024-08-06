from sys import stdin
from collections import defaultdict


def solution():
    n, k, t, m = map(int, stdin.readline().split())
    p = {team: defaultdict(int) for team in range(1, n + 1)}
    submit = {team: defaultdict(int) for team in range(1, n + 1)}
    team_sum = dict()
    for c in range(m):
        i, j, s = map(int, stdin.readline().split())
        p[i][j] = max(p[i][j], s)
        # 제출 횟수 / 제출 시간
        submit[i] = (submit[i][0] + 1, c)
    for k in p.keys():
        team_sum[k] = (sum(p[k].values()), submit[k][0], submit[k][1])
    for i, team in enumerate(sorted(team_sum.items(), key=lambda x: (-x[1][0], x[1][1], x[1][2])), start=1):
        if team[0] == t:
            print(i)
            break


for _ in range(int(stdin.readline())):
    solution()
