def solution(ingredient):
    answer = 0
    p = 0
    h = []
    c = [1, 2, 3, 1]
    cl = len(c)
    for i in ingredient:
        h.append(i)
        if len(h) < 4:
            continue
        if h[-4:] == c:
            for j in range(4):
                h.pop()
            answer += 1

    return answer
