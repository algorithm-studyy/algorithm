def solution(arr):
    answer = []
    for item in arr:
        if answer and answer[-1] == item:
            continue
        answer.append(item)
    return answer
