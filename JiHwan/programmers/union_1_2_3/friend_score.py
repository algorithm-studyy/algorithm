def solution(name, yearning, photo):
    answer = []
    score = dict(zip(name, yearning))
    for p in photo:
        total = 0
        for i in p:
            if i not in score:
                total += 0
            else:
                total += score[i]
        answer.append(total)
    return answer