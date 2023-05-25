# 1. 연산자의 우선순위를 바꾸기 O
# 2. 중위 -> 후위
# 3. 가장 큰 절대값 구하기
from itertools import permutations


def get_operand(e):
    result = set()
    for c in e:
        if c in '+-*':
            result.add(c)
    return list(result)


def get_list_expression(e):
    result = []
    i = 0
    while i < len(e):
        if e[i] in '*-+':
            result.append(e[i])
            i += 1
            continue
        s = 0
        while i + s < len(e) and e[i + s] not in '*-+':
            s += 1
        result.append(e[i:i + s])
        i += s
    return result


def infix_to_postfix(e, op_rank):
    operator = []
    result = []
    for t in e:
        if t not in '-*+':
            result.append(t)
            continue
        while operator and op_rank[operator[-1]] >= op_rank[t]:
            result.append(operator.pop())
        operator.append(t)
    while operator:
        result.append(operator.pop())
    return result


def calculate_postfix(e):
    stack = []
    for t in e:
        if t not in '*-+':
            stack.append(t)
        else:
            a2, a1 = map(int, [stack.pop(), stack.pop()])
            if t == '*':
                stack.append(a1 * a2)
            elif t == '-':
                stack.append(a1 - a2)
            elif t == '+':
                stack.append(a1 + a2)
    return abs(stack[0])


def solution(expression):
    answer = 0
    operator = get_operand(expression)
    list_expr = get_list_expression(expression)
    for op in permutations(operator):
        op_rank = {k: v for v, k in enumerate(op)}
        postfix = infix_to_postfix(list_expr, op_rank)
        calculate_result = calculate_postfix(postfix)
        answer = calculate_result if calculate_result > answer else answer
    return answer

