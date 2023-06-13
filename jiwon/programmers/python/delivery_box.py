# if o > arr[0] while popleft
# else:
#  if stack[-1] == o
#     continue
#  elif stack[-1] > o: stack.pop()
#  else: return answer
from collections import deque


def solution(order):
    answer = 0
    arr = deque([i + 1 for i, v in enumerate(order)])
    stack = []
    for o in order:
        if arr and o >= arr[0]:
            while arr and arr[0] != o:
                stack.append(arr.popleft())
            if arr and arr[0] == o:
                arr.popleft()
                answer += 1
        else:
            if stack and stack[-1] == o:
                stack.pop()
                answer += 1
            else:
                return answer
    return answer
