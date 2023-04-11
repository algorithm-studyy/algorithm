def solution(s):
    answer = True
    arr = list(s)
    stack = []

    if arr[0] == ')':
        answer = False

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
        else:
            if stack == []:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        answer = False

    return answer