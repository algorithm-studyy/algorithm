class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        for i in range(0, len(nums), 2):
            result.append(min(nums[i:i + 2]))
        return sum(result)
