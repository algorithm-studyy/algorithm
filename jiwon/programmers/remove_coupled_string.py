# 준비물 : 스택, deque
# 1. deque에서 일단 popleft()
# 2. 스택 안에 값이 있으면, 스택 top == pop값이 같은지 비교
# 2-1. top이 같으면 스택 pop
# 2-2. 다르면 스택에 push
# 3. 스택에 값이 존재하면 0, 없으면 1

from collections import deque

def solution(s):
    dq = deque(list(s))
    stack = []
    while dq:
        val = dq.popleft()
        if stack and stack[-1] == val:
            stack.pop()
        else:
            stack.append(val)

    return 0 if stack else 1
