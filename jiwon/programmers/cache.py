# 캐시 크기 : 큐의 길이
# 큐에 존재하면 hit
# 1. hit한 거 pop
# 2. append
# 큐에 존재하지 않으면
# 1. popleft
# 2. append

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer
