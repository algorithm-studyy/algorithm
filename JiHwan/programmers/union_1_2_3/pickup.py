def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    num_deli = 0
    num_pick = 0
    for i in range(n):
        num_deli += deliveries[i]
        num_pick += pickups[i]

        while num_deli > 0 or num_pick > 0:
            num_deli -= cap
            num_pick -= cap
            answer += (n - i) * 2
        #            택배가 출발을 했으면 되돌아와야 하기 때문에 x2를 진행

    return answer