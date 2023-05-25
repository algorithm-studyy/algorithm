def solution(name, yearning, photo):
    answer = []
    score = {k: v for k, v in zip(name, yearning)}
    for people in photo:
        people_score = 0
        for person in people:
            if person in score:
                people_score += score[person]
        answer.append(people_score)
    return answer
