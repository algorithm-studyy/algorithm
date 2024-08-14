N, M = map(int, input().split())
before_heights = list(map(int, input().split()))
rainy_days = [list(map(int, input().split())) for _ in range(M)]
water_heights = [0] * N

for i in range(M):
    start, end = rainy_days[i]
    for j in range(start - 1, end):
        water_heights[j] += 1

    if (i + 1) % 3 == 0:
        recent_rainy_days = set()
        for k in range(max(0, i - 2), i + 1):
            s, e = rainy_days[k]
            recent_rainy_days.update(range(s - 1, e))

        for idx in recent_rainy_days:
            if water_heights[idx] > 0:
                water_heights[idx] -= 1

final_heights = [h + w for h, w in zip(before_heights, water_heights)]
print(" ".join(map(str, final_heights)))