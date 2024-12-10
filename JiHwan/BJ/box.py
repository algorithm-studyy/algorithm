def solution(order):
    answer = 0
    stack = []

    for idx, value in enumerate(order):
        stack.append(idx + 1)

        while stack and stack[-1] == order[answer]:
            stack.pop()
            answer += 1

    return answer


print(solution([4, 3, 1, 2, 5]))