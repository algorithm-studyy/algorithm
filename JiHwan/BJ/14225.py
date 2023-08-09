from itertools import combinations

n = int(input())
s = list(map(int, input().split()))

sum_list = []
for i in range(1, n+1):
    comb_list = list(combinations(s, i))
    for j in comb_list:
        sum_list.append(sum(j))

for i in range(1, max(sum_list)+1):
    if i not in sum_list:
        print(i)