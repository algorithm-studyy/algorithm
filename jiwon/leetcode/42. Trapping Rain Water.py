class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        left = 0
        right = len(height) - 1
        answer = 0
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max <= right_max:
                answer += left_max - height[left]
                left += 1
            else:
                answer += right_max - height[right]
                right -= 1
        return answer