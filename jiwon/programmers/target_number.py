answer = 0


def dfs(depth, hap, numbers, target):
    global answer
    if depth == len(numbers):
        answer = answer + 1 if hap == target else answer
        return
    dfs(depth + 1, hap + numbers[depth], numbers, target)
    dfs(depth + 1, hap - numbers[depth], numbers, target)


def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer
