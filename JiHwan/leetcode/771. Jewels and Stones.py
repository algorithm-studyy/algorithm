from itertools import combinations
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for i in stones:
            if i in jewels:
                answer += 1
        return answer