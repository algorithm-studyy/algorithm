from collections import Counter

N, X = map(int, input().split())
visitor = list(map(int, input().split()))

default = sum(visitor[:X])
sum_visitor = [default]

for i in range(1, N - X - 1):
    default = default - visitor[i - 1] + visitor[i + (X - 1)]
    sum_visitor.append(default)

count_period = Counter(sum_visitor)
if max(sum_visitor) != 0:
    print(max(sum_visitor))
    print(count_period[max(sum_visitor)])
else:
    print("SAD")
