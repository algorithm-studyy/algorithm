from itertools import permutations, zip_longest
from collections import deque
from sys import stdin


# 우선 순위 없을때
def cal_nums(operand, operator):
    cals = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y if x > 0 else -(-x // y),
    }
    num = operand.popleft()
    while operand:
        num = cals[operator.popleft()](num, operand.popleft())
    return num


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
m = list(map(int, stdin.readline().split()))
op = ['+', '-', '*', '/']
op_list = [op[i] for i, v in enumerate(m) for _ in range(v)]
results = []
for ops in permutations(op_list):
    results.append(cal_nums(deque(arr), deque(ops)))

print(max(results))
print(min(results))

# 우선 순위 있을 때
# def cal_nums(operand, operator):
#     expression = ''.join(op1 + op2 for op1, op2 in zip_longest(operand, operator, fillvalue=''))
#     print(expression)
#     return eval(expression)
#
#
# n = int(stdin.readline())
# arr = stdin.readline().split()
# m = list(map(int, stdin.readline().split()))
# op = ['+', '-', '*', '//']
# op_list = [op[i] for i, v in enumerate(m) for _ in range(v)]
# results = []
# for ops in permutations(op_list):
#     results.append(cal_nums(arr, ops))
# print(results)
# print(max(results))
# print(min(results))
