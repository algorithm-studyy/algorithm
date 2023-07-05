class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_set = {nums[0]}
        answer = set()
        for i in range(1, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in num_set:
                    answer.add(tuple(sorted([-(nums[i] + nums[j]), nums[i], nums[j]])))
            num_set.add(nums[i])
        return answer
    