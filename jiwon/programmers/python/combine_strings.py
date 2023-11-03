from collections import defaultdict

def solution(strArr):
    dic = defaultdict(int)
    for s in strArr:
        dic[len(s)] += 1
    return max(dic.values())
