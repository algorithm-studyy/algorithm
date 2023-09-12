def solution(answers):
    answer = [0] * 3
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if ans_1[i % len(ans_1)] == answers[i]:
            answer[0] = answer[0] + 1
        if ans_2[i % len(ans_2)] == answers[i]:
            answer[1] = answer[1] + 1
        if ans_3[i % len(ans_3)] == answers[i]:
            answer[2] = answer[2] + 1

    max_answer = max(answer)
    answer_index = [i + 1 for i, v in enumerate(answer) if v == max_answer]
    answer_index.sort(reverse=False)
    return answer_index