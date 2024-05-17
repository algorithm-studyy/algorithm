

def change_post_expr():
    operand = []
    result = []
    input()
    for c in input():
        if c.isdigit():
            result.append(int(c))
        else:
            if operand:
                while operand and priority[operand[-1]] >= priority[c]:
                    result.append(operand.pop())
                operand.append(c)
            else:
                operand.append(c)
    while operand:
        result.append(operand.pop())
    return result


priority = {v: i for i, v in enumerate(['+'])}
for test_case in range(1, 11):
    post = change_post_expr()
    answer = post[0]
    for index in range(1, len(post) - 1, 2):
        if post[index + 1] == '+':
            answer += post[index]

    print('#%d %d' % (test_case, answer))
