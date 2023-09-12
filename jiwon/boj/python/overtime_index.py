# N 시간 피로도 최소
# N 시간당 N만큼 처리

# works를 균등하게 일을 해야함 -> How
# But. 균등하게 일을 할 수가 없음 ..
# 일을 다시 주는건 불가능하기 때문
# 기존에서 큰값에서만 빼야하나 .. ?
# sum(works) = 10 // n -> 2.xxx
# sum(works) = 5 // n -> 5
from heapq import heappush, heappop, heapify


def solution(n, works):
    heap = []
    for w in works:
        heappush(heap, -w)
    while n:
        w = heappop(heap)
        if w == 0:
            break
        n -= 1
        heappush(heap, w + 1)
    return sum([v ** 2 for v in heap])