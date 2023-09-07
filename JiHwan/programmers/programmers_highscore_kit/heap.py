def solution(operations):
    answer = []
    stack = []
    for i in range(len(operations)):
        oper, num_str = operations[i].split()
        num = int(num_str)

        if oper == 'I':
            stack.append(num)
        elif oper == 'D' and num == 1:
            if stack:
                stack.remove(max(stack))
        elif oper == 'D' and num == -1:
            if stack:
                stack.remove(min(stack))

    if len(stack) == 0:
        answer = [0, 0]
    else:
        answer.append(max(stack))
        answer.append(min(stack))

    return answer