class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                if target in nums[j + 1:]:
                    answer.append([nums[i], nums[j], target])

        filtered_answer = list(set(map(tuple, answer)))
        result = [list(item) for item in filtered_answer]
        return result


