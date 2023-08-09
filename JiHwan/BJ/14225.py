from itertools import combinations
from collections import Counter

n = int(input())
s = list(map(int, input().split()))

sum_list = []
for i in range(1, n+1):
    comb_list = list(combinations(s, i))
    for j in comb_list:
        sum_list.append(sum(j))


list_count = Counter(sum_list)

for i in range(1, 2**n + 1):
    if i not in list_count:
        print(i)
        break
