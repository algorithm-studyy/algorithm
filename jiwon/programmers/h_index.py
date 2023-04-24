# n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면
# h의 최댓값이 이 과학자의 H-index입니다.


def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(1, len(citations) + 1):
        if citations[i - 1] >= i:
            answer += 1
        else:
            break
    return answer
