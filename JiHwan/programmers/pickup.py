def solution(cap, n, deliveries, pickups):
    answer = -1
    sum_deliveries = sum(deliveries)
    sum_pickups = sum(pickups)
    while True:
        if sum_deliveries == 0 and sum_pickups == 0:
            return answer
        else:
            for i in deliveries[::-1]:





