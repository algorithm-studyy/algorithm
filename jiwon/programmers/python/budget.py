def solution(d, budget):
    d.sort()
    answer = 0
    for c in d:
        if budget >= c:
            budget -= c
            answer += 1
        else:
            break
    return answer


print(solution([1,3,2,5,4],	9))
