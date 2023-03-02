def dfs(idx, cnt, nums, m, path):
    if cnt == m:
        print(' '.join(path))
        return

    for i in range(idx, len(nums)):
        dfs(i+1, cnt+1, nums, m, path+[nums[i]])

n, m = map(int, input().split())
nums = input().split()
nums.sort()

dfs(0, 0, nums, m, [])