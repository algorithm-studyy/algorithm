
from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    print(counter)
    tangerine.sort(key = lambda t: (-counter[t], t))
    print(tangerine)
    print(tangerine[:k])
    print(set(tangerine))
    print(set(tangerine[:k]))
    return len(set(tangerine[:k]))


solution(6, 	[1, 3, 2, 5, 4, 5, 2, 3])