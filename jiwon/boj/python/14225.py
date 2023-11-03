from sys import stdin
from itertools import combinations

n = int(stdin.readline())
s = list(map(int, stdin.readline().split()))

a = {x for x in range(1, sum(s) + 2)}
b = set()
for i in range(1, len(s) + 1):
    for nums in combinations(s, i):
        b.add(sum(nums))

print(min(a - b))
