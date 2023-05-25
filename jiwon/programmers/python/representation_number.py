def solution(n):
    answer = 0

    for i in range(n):
        hap = 0
        for j in range(i + 1, n + 1):
            hap += j
            if hap == n:
                answer += 1
            if hap > n:
                break

    return answer
