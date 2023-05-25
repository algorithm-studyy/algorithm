from collections import Counter


# 오른쪽과 왼쪽을 나누어서 딕셔너리를 사용
def solution(topping):
    answer = 0
    left_dic = dict()
    right_dic = Counter(topping)
    for i, t in enumerate(topping):
        left_dic[t] = left_dic[t] + 1 if t in left_dic else 1
        right_dic[t] -= 1
        if right_dic[t] == 0:
            del right_dic[t]
        answer += 1 if len(left_dic) == len(right_dic) else 0
    return answer
