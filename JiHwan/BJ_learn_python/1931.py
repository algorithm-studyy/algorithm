N = int(input())

time = []
for i in range(N):
    s_t, e_t = map(int, input().split())
    time.append([s_t, e_t])
time.sort(key=lambda a: a[0])
time.sort(key=lambda a: a[1])

last = 0
count = 0

for i, j in time:
    if i >= last:
        count += 1
        last = j
print(count)