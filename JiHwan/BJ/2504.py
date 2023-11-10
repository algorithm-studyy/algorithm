from sys import stdin


def solution():
    global result
    answer = 1

    for i, c in enumerate(line):
        if c == "]":
            answer *= 3
            stack.append(c)
            if not stack or stack[-1] != "]":
                print(0)
                return
            if line[i - 1] == "[":
                stack.pop(i)
                result += answer
                answer //= 3

        elif i == ")":
            answer *= 2
            stack.append(c)
            if not stack or stack[-1] != ")":
                print(0)
                return
            if line[i - 1] == "(":
                stack.pop(i)
                result += answer
                answer //= 2
    if stack:
        print(0)
    else:
        print(result)


if __name__ == '__main__':
    line = stdin.readline().strip()
    stack = []
    result = 0
    solution()
