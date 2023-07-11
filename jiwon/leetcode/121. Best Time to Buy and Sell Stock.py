from heapq import heappop, heappush


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = 1e9
        answer = 0
        for p in prices:
            num = min(num, p)
            answer = max(answer, p - num)
        return answer
