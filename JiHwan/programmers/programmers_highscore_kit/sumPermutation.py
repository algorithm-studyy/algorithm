def solution(elements):
    answer = len(result)
    result = set()
    circle = elements + elements

    for i in range(len(elements)):
        for j in range(len(elements)):
            result.add(sum(circle[i: i + j + 1]))

    return answer
