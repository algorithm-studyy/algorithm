from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
operator = ['+', '-', '*', '/']
num_operator = list(map(int, input().split()))
operation = [op for op, num in zip(operator, num_operator) for _ in range(num) if num != 0]

max_num, min_num = -1e9, 1e9

for case in permutations(operation, n - 1):
    total = a[0]
    for i in range(1, n):
        if case[i - 1] == '+':
            total += a[i]
        elif case[i - 1] == '-':
            total -= a[i]
        elif case[i - 1] == '*':
            total *= a[i]
        elif case[i - 1] == '/':
            if total < 0:
                total = int(abs(total)/a[i])
            else:
                total = int(total / a[i])

    if total > max_num:
        max_num = total
    if total < min_num:
        min_num = total
print(max_num)
print(min_num)
