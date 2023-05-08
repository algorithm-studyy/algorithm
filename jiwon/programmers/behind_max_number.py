# 어떻게 하면 시간복잡도를 줄일 수 있을까?
# 다시풀기

def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i, v in enumerate(numbers):
        while stack and numbers[stack[-1]] < v:
            answer[stack.pop()] = v
        stack.append(i)
    return answer
