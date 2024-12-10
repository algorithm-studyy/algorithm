import math

N = int(input())
stations = list(map(int, input().split()))
W = int(input())

answer = 0
cover = 2 * W + 1

now = 1
for station in stations:
    length = station - W - now
    if length > 0:
        answer += math.ceil(length / cover)
    now = station + W + 1
if N >= now:
    answer += math.ceil((N - now + 1) / cover)

print(answer)
