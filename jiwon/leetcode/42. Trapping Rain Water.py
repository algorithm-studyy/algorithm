# 1. 0이 아닌 것이 나오면 left
# 2. 0이 아니고 min(left) < h라면, min(max(left), h)
# 3. min(left)

class Solution:
    def get_custom_min(self, lst):
        result = 1e9
        for item in lst:
            if 0 < item < result:
                result = item
        return result
    def trap(self, height: list[int]) -> int:
        left = []
        answer = 0
        for i, h in enumerate(height):
            if not left and h > 0:
                left.append(h)
            elif left and self.get_custom_min(left) < h:
                max_h = min(max(left), h)
                for item in left:
                    answer += max(max_h - item, 0)
                left = [h]
            elif left:
                left.append(h)

            print('left = ', left, ' / i = ', i, ' / h = ', h, ' / answer = ', answer)
        return answer


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,0,3,2,5]))
