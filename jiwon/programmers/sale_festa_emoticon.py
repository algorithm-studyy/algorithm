# 개별로 이모티콘 할인 적용되어야 한다.
from itertools import product


def get_discount_emoticons(emoticons, percents):
    return [int(emoticon * (100 - percents[i]) / 100) for i, emoticon in enumerate(emoticons)]


def get_result(users, emoticons, percents):
    emoticon_plus, take = [0, 0]
    for percent, money in users:
        sum_by_percent = 0
        for i, emoticon in enumerate(emoticons):
            sum_by_percent = sum_by_percent + emoticon \
                if percents[i] >= percent else sum_by_percent
        if sum_by_percent >= money:
            emoticon_plus += 1
        else:
            take += sum_by_percent
    return emoticon_plus, take


def solution(users, emoticons):
    answer = []
    for percents in product([10, 20, 30, 40], repeat=len(emoticons)):
        discount_price = get_discount_emoticons(emoticons, percents)
        answer.append(get_result(users, discount_price, percents))
    return sorted(answer, key=lambda x: (x[0], x[1]), reverse=True)[0]
