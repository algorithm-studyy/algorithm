from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
operator = ['+', '-', '*', '/']
num_operator = list(map(int, input().split()))
operation = [op for op, num in zip(operator, num_operator) for _ in range(num) if num != 0]

max_num, min_num = -1e9, 1e9

for case in permutations(operation, n - 1):
    total = nums[0]
    for i in range(1, n):
        if case[i - 1] == '+':
            total += nums[i]
        elif case[i - 1] == '-':
            total -= nums[i]
        elif case[i - 1] == '*':
            total *= nums[i]
        elif case[i - 1] == '/':
            if total < 0:
                # total = int(abs(total)/nums[i])    다시 마이너스
            else:
                total = int(total / nums[i])

    if total > max_num:
        max_num = total
    if total < min_num:
        min_num = total

print(max_num)
print(min_num)
