from heapq import heappush, heappop


def solution(n, k, enemy):
    answer = 0
    if len(enemy) <= k or sum(enemy) <= n:
        return len(enemy)
    heap = []
    for e in enemy:
        heappush(heap, (-e, e))
        n -= e
        if n < 0 and k <= 0:
            break
        while heap and n < 0 < k:
            n += heappop(heap)[1]
            k -= 1
        answer += 1
    return answer
