def solution(s):
    stack = []
    for b in s:
        if b == '(':
            stack.append(b)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True
