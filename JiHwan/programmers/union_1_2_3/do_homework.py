# 진행중이던 과제가 끝나고 새로 시작할 과제 시간이 되지 않았을 때 못다한 과제를 한다.
# plans[1]의 start - (plans[0]의 start + playtime) > 0 이면 못다한 과제 진행
# 과제를 다 못한 과목은 not_yet에 저장해 둔다.
# 과제를 다 진행한 과목은 answer에 append 한다.


def sorted_time(plans):
    for i, p in enumerate(plans):
        h, m = map(int, p[1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    return sorted(plans, key=lambda x: x[1])


def solution(plans):
    answer = []
    not_yet = []
    plans = sorted_time(plans)

    for i in range(len(plans)):
        if plans[i][1] + plans[i][2] <= plans[i + 1][1]: