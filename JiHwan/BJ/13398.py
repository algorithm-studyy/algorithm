n = int(input())
a = list(map(int, input().split()))
hap = [a[0]]
sum_1 = [a[0]]

for i in range(len(a) - 1):
    hap.append(max(hap[i] + a[i + 1], a[i + 1]))

a = [x for x in a if x >= 0 or max(hap) >= abs(x)]

for i in range(len(a)-1):
    sum_1.append(max(sum_1[i] + a[i + 1], a[i + 1]))


print(max(sum_1))

