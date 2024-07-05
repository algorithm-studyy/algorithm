n, m = map(int, input().split())
hap = [0 for _ in range(n)]

for i in range(n):
    score = list(map(int, input().split()))
    total = score[1] * 3 + score[2] * 2 + score[3]
    hap[score[0] - 1] = total

result = sorted(set(hap), reverse=True)
print(result.index(hap[m - 1]) + 1)

