class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        result = 0
        for s in stones:
            if s in j:
                result += 1

        return result
