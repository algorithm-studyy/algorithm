# 1. 회전
# 2. 올바른 괄호인지 판단

from collections import deque


def solution(s):
    answer = 0
    bracket = {b: i for i, b in enumerate('({[)}]')}
    q = deque(s)
    for i in range(len(s)):
        stack = []
        for value in q:
            if bracket[value] < 3:
                stack.append(value)
            else:
                if stack and bracket[value] - bracket[stack[-1]] == 3:
                    stack.pop()
                else:
                    break
        else:
            answer += 0 if stack else 1

        q.append(q.popleft())
    return answer
