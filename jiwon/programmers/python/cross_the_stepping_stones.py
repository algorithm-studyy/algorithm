# 디딤돌의 숫자는 한 번 밟을 때 1씩 줄어듦
# 디딤돌의 숫자가 0이면 더 이상 밟을 수 없음
# 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건널 수 있음

# 최대 갈 수 있는 칸수 k
# 한 명씩만 건널 수 있음
def is_cross(stones, num, k):
    cnt = 0
    for stone in stones:
        cnt = cnt + 1 if stone <= num else 0
        if cnt >= k:
            return False
    return True


def solution(stones, k):
    start, end = 1, max(stones)
    while start <= end:
        mid = (start + end) // 2
        if is_cross(stones, mid, k):
            start = mid + 1
        else:
            end = mid - 1
    return start
