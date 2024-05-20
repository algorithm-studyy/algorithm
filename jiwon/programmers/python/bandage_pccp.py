def solution(bandage, health, attacks):
    answer = health
    pre_time = 0
    for time, damage in attacks:
        time_diff = time - pre_time
        healing = time_diff * bandage[1] + time_diff // bandage[0] * bandage[2]
        answer = min(health, answer + healing)

        answer -= damage
        pre_time = time + 1

        if answer <= 0:
            return -1
    return answer