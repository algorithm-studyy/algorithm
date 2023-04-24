
def solution(citations):
    citations.sort(reverse=True)
    temp = map(min, enumerate(citations, start=1))
    print(list(temp))
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


print(solution([3, 0, 6, 1, 5]))
