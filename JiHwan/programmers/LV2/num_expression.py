def solution(n):
    answer = 0
    sum = 0
    for i in range(1, n):
        for j in range(i, n):
            sum += j
            if sum > n:
                sum = 0
                break
            if sum == n:
                sum = 0
                answer += 1
                break

    return answer + 1