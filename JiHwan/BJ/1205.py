import sys

n, new, p = map(int, sys.stdin.readline().split())

if n == 0:
    print(1)
else:
    rank = list(map(int, sys.stdin.readline().split()))
    if n == p and rank[-1] >= new:
        print(-1)
    else:
        rank.append(new)
        new_rank = sorted(rank, reverse=True)
        print(new_rank.index(new) + 1)
