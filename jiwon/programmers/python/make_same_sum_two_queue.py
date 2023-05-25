# 큰쪽에서 빼면 자연스럽게 되지 않을까
from collections import deque


def solution(queue1, queue2):
    answer = 0
    s1, s2 = sum(queue1), sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)
    limit = len(q1) * 3
    while answer < limit:
        if s1 == s2:
            return answer
        elif s1 > s2:
            s1 -= q1[0]
            s2 += q1[0]
            q2.append(q1.popleft())
        else:
            s1 += q2[0]
            s2 -= q2[0]
            q1.append(q2.popleft())
        answer += 1

    return -1
