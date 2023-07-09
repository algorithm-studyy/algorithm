# 어떻게 푸는 지 확인하기
# def solution(plans):
#     plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])
#
#     lst = []
#     while plans:
#         x = plans.pop()
#         for i, v in enumerate(lst):
#             if v[0] > x[1]:
#                 lst[i][0] += x[2]
#         lst.append([x[1] + x[2], x[0]])
#     lst.sort()
#
#     return list(map(lambda x: x[1], lst))

# 1. start_time 정렬
# 2. 시작! : 시작 시간 + playtime - 다음 시작
# 비는 시간이 있으면 그 사이에는 잠시 멈춘 과제를 해야한다.
# 비는 시간인지 확인 ? start_time - prev_end_time > 0 = 비는 시간
# pause_time - (start_time - prev_end_time) <= 0  -> answer.append()
# else pause_time[1] -= start_time - prev_end_time


def get_sorted_list_by_time(plans):
    for i, p in enumerate(plans):
        h, m = map(int, p[1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    return sorted(plans, key=lambda x: x[1])


def solution(plans):
    answer = []
    stack = []
    plans = get_sorted_list_by_time(plans)
    for i in range(1, len(plans)):
        start_time = plans[i][1]
        prev_end_time = plans[i - 1][1] + plans[i - 1][2]
        time_diff = start_time - prev_end_time
        if time_diff >= 0:
            answer.append(plans[i - 1][0])
            while stack and time_diff > 0:
                if stack[-1][2] <= time_diff:
                    time_diff -= stack[-1][2]
                    answer.append(stack.pop()[0])
                else:
                    stack[-1][2] -= time_diff
                    time_diff = 0
        else:
            plans[i - 1][2] = -time_diff
            stack.append(plans[i - 1])
    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    return answer

