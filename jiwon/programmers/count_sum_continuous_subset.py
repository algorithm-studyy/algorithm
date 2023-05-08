# 원형 수열로 만들 수 있는 부분 수열의 합의 개수


def solution(elements):
    answer = set()

    #######################
    # 기존 코드
    # arr = elements + elements
    # for i in range(1, len(elements) + 1):
    #     for j in range(len(elements)):
    #         hap = sum(arr[j:j+i])
    #         answer.add(hap)

    # 개선 코드
    for i, v in enumerate(elements):
        hap = 0
        for j in range(i, i + len(elements)):
            hap += elements[j % len(elements)]
            answer.add(hap)
    return len(answer)
