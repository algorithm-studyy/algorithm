class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = n + nums[left] + nums[right]
                if val < 0:
                    left += 1
                elif val > 0:
                    right -= 1
                else:
                    answer.append([n, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return answer