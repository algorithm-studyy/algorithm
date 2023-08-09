from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

val = 0
start = 0
end = 0
cnt = 0
while start <= end <= n:
    if val == m:
        cnt += 1
    if val >= m:
        val -= nums[start]
        start += 1
    else:
        if end < n:
            val += nums[end]
        end += 1

print(cnt)
