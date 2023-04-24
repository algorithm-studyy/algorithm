# 중복된 원소, 순서가 다르면 다른 튜플, 튜플의 원소 개수는 유한
# 개수가 제일 많은 것이 먼저 오게끔만 하면 됨

import re


def solution(s):
    dic = dict()
    for tup in re.sub('[{}]', '', s).split(','):
        dic[tup] = dic[tup] + 1 if tup in dic else 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return [int(k) for k, v in dic]
