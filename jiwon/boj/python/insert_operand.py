from sys import maxsize

max_value = -maxsize
min_value = maxsize


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    op = {k: v for v, k in zip(list(map(int, input().split())), ['+', '-', '*', '/'])}
    recursive(0, arr, op, arr[0])
    print(max_value)
    print(min_value)


def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a // b if a > 0 else -(-a // b)


def recursive(d, arr, op, result):
    global max_value, min_value
    if d + 1 == len(arr):
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    for k, v in op.items():
        if op[k]:
            op[k] -= 1
            recursive(d + 1, arr, op, calc(result, arr[d + 1], k))
            op[k] += 1


solution()
