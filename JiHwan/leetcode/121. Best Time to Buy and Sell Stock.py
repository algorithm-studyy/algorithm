# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_price = 0
#         if sorted(prices, reverse=True) == prices:
#             return max_price
#         for i in range(len(prices)):
#             for j in range(i, len(prices)):
#                 max_price = max(prices[j] - prices[i], max_price)
#         return max_price


    ##타임아웃 발생

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = sys.maxsize
        answer = 0
        for i in prices:
            num = min(num, i)
            answer = max(answer, i - num)
        return answer


