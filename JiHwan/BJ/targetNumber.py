def solution(numbers, target):
    answer = 0
    result = [0]

    for num in numbers:
        visited = []
        for node in result:
            visited.append(node + num)
            visited.append(node - num)
        result = visited

    for node in result:
        if node == target:
            answer += 1

    return answer