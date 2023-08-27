def solution(n):
    answer = 0
    fibo = [0] * 100000
    fibo[1] = 1
    fibo[2] = 1
    fibo[3] = 2

    if n == 1:
        answer = 1
    elif n == 2:
        answer = 1
    elif n == 3:
        answer = 2
    else:
        for i in range(4, n + 1):
            fibo[i] = fibo[i - 2] + fibo[i - 1]
    answer = fibo[n] % 1234567
    return answer