def solution(survey, choices):
    answer = ''
    t = {k: 0 for k in ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']}
    zip_k = [(a, b) for a, b in zip(['R', 'C', 'J', 'A'], ['T', 'F', 'M', 'N'])]
    score = [i for i in range(3, -1, -1)]

    for i in range(len(survey)):
        c = choices[i]
        if c > 4:
            t[survey[i][1]] += score[7 - c]
        else:
            t[survey[i][0]] += score[c - 1]
    for k1, k2 in zip_k:
        if t[k1] < t[k2]:
            answer += k2
        elif t[k1] > t[k2]:
            answer += k1
        else:
            answer += sorted([k1, k2])[0]

    return answer
