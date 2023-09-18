# 양쪽을 못뜯음
# 원형이라 다시 돌 수도 있음
# 2, 3 뜯기
def solution(sticker):
    answer = 0
    n = len(sticker)
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp2 = [0] * n
    route = [{i} for i in range(n)]
    for i in range(1, n):
        dp1[i] += max(dp1[i - 2] + sticker[i], dp1[i - 1])
    print(dp1)
    return max(dp1[n - 1], )