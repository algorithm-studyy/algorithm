def hanoi(n, start, mid, end):
    global answer
    if n == 1:
        answer.append([start, mid])
    else:



def solution(n):
    global answer
    answer = []
    hanoi(n, 1, 2, 3)
    return answer