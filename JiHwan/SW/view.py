n = int(input())
height = list(map(int, input().split()))
answer = 0
max_height = 0
for i in range(2, n - 1):
    if height[i] > height[i - 1] and height[i] > height[i - 2] and height[i] > height[i + 1] and height[i] > height[i + 2]:
        max_height = max(height[i - 2], height[i - 1], height[i + 1], height[i + 2])
        answer = answer + (height[i] - max_height)
print(answer)
