# 디딤돌의 숫자는 한 번 밟을 때 1씩 줄어듦
# 디딤돌의 숫자가 0이면 더 이상 밟을 수 없음
# 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건널 수 있음

# 최대 갈 수 있는 칸수 k
# 한 명씩만 건널 수 있음

# 작은 구간을 만났을 때 그 구간이 가장 k만큼 이면 끝
# stone -> 2, 4, 5
# min(max, k)
from sys import maxsize


def solution(stones, k):
    answer = maxsize
    s = 0
    while s + k <= len(stones):
        part = max(stones[s:s + k])
        answer = min(answer, part)
        s += 1
    return answer