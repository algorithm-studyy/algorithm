#runtime: 242ms, memory 23.5mb
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        num = 1

        for i in range(0, len(nums)):
            answer.append(num)
            num = num * nums[i]

        num = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] = num * answer[i]
            num = num * nums[i]

        return answer



