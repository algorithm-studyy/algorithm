# 2 * 2 + 2 * 3 * 3 + 2 * 3 = 4 + 18 + 6
#

from sys import stdin


def postprocessing(num, index):
    print(stack, index, num)
    while stack and index < len(line):
        if stack[-1] == '[' and line[index] == ']':
            num //= 3
            if not stack or stack[-1] != '[':
                print(0)
                exit(0)
            stack.pop()
        elif stack[-1] == '(' and line[index] == ')':
            num //= 2
            if not stack or stack[-1] != '(':
                print(0)
                exit(0)
            stack.pop()
        else:
            break
        index += 1
    print(stack, index, num)
    return num, index


def solution():
    result = 0
    num = 1
    index = 0
    while index < len(line):
        c = line[index]
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
            stack.pop()
            result += num
            num, index = postprocessing(num, index + 1)
        elif c == ")":
            if not stack or stack[-1] != '(':
                print(0)
                return
            stack.pop()
            result += num
            num, index = postprocessing(num, index + 1)
        index += 1
    print(result)


if __name__ == '__main__':
    line = stdin.readline().strip()
    stack = []
    solution()
