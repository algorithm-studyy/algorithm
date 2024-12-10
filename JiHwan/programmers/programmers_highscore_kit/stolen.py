def solution(money):
    answer = 0
    if len(money) == 1:
        return money.pop()
    dp1 = [0] + money[:-1]
    for i in range(2, len(money)):
        dp1[i] = max(dp1[i] + dp1[i -2], dp1[i - 1])
    dp2 = [0] + money[1:]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i] + dp2[i - 2], dp2[i - 1])
    answer = max(dp1[-1], dp2[-1])
    return answer