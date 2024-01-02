def solution(bandage, health, attacks):
    answer = health
    healing = 0
    t = 0
    max_time = attacks[-1][0]
    at = {}

    for i in range(len(attacks)):
        at[attacks[i][0]] = attacks[i][1]

    while t <= max_time:

        if t in at:
            healing = 0
            answer -= at[t]

            if answer <= 0:
                return -1
        else:
            healing += 1
            if healing < bandage[0]:
                answer += bandage[1]
                if answer > health:
                    answer = health
            else:
                answer += bandage[1] + bandage[2]
                if answer > health:
                    answer = health
                healing = 0
        t += 1

    return answer
