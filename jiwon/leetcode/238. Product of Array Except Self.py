class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = [1] * len(nums)
        arr2 = [1] * len(nums)
        for i in range(len(nums) - 1):
            arr1[i + 1] = arr1[i] * nums[i]
        for i in range(len(nums) - 1, 0, -1):
            arr2[i - 1] = arr2[i] * nums[i]
        return [arr1[i] * arr2[i] for i, v in enumerate(arr1)]