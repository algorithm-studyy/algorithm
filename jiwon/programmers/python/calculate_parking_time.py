# 출차된 내역이 없으면 23:59 출차
# ceil(누적 주차 시간 - 단위 시간 / 10) x 600
from math import ceil


def get_car_number(records):
    dic = {}
    for record in records:
        hours, number, in_out = record.split(' ')
        hour, minute = hours.split(':')
        total_min = int(hour) * 60 + int(minute)
        if number in dic:
            dic[number].append(total_min)
        else:
            dic[number] = [total_min]
    return dic


def solution(fees, records):
    answer = []
    dic = get_car_number(records)
    for key in sorted(dic.keys()):
        i = 0
        park_time = 0
        if len(dic[key]) % 2 == 1:
            dic[key].append(23 * 60 + 59)
        while i < len(dic[key]):
            park_time += dic[key][i + 1] - dic[key][i]
            i += 2
        answer.append(fees[1] + ceil(max(park_time - fees[0], 0) / fees[2]) * fees[3])
    return answer
