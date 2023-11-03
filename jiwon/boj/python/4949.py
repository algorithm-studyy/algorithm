from sys import stdin


def check_balance():
    stack = []
    for item in line:
        if item in '([':
            stack.append(item)
        elif item == ']':
            if not stack or stack[-1] != '[':
                print('no')
                return
            stack.pop()
        elif item == ')':
            if not stack or stack[-1] != '(':
                print('no')
                return
            stack.pop()
    if stack:
        print('no')
    else:
        print('yes')


if __name__ == '__main__':
    while True:
        line = stdin.readline().rstrip()
        if len(line) == 1 and line[0] == '.':
            break
        check_balance()

