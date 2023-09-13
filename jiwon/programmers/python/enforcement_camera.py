# 단속용 카메라를 한 번은 만나도록 카메라를 설치
# 모든 차량이 한 번은 단속용 카메라를 만나려면 최소 몇 대의 카메라를 설치

def solution(routes):
    answer = 0
    point = -1e9
    for s, e in sorted(routes, key=lambda x: (x[1], x[0])):
        if s <= point <= e:
            continue
        answer += 1
        point = e
    return answer
