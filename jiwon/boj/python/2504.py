# 2 * 2 + 2 * 3 * 3 + 2 * 3 = 4 + 18 + 6
#

from sys import stdin


def solution():
    global result
    num = 1
    for i, c in enumerate(line):
        if c == "[":
            num *= 3
            stack.append(c)
        elif c == "(":
            num *= 2
            stack.append(c)
        elif c == "]":
            if not stack or stack[-1] != '[':
                print(0)
                return
            result += num if line[i - 1] == '[' else 0
            num //= 3
            stack.pop()
        elif c == ")":
            if not stack or stack[-1] != '(':
                print(0)
                return
            result += num if line[i - 1] == '(' else 0
            num //= 2
            stack.pop()
    if stack:
        print(0)
    else:
        print(result)


if __name__ == '__main__':
    line = stdin.readline().strip()
    stack = []
    result = 0
    solution()
