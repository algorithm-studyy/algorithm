from sys import stdin

n, k = map(int, stdin.readline().split())
c = []
target = list()
result = 1
for _ in range(n):
    lst = list(map(int, stdin.readline().split()))
    if k == lst[0]:
        target = lst
    else:
        c.append(lst)

for item in c:
    if item[1] > target[1]:
        result += 1
    elif item[1] == target[1] and item[2] > target[2]:
        result += 1
    elif item[1] == target[1] and item[2] == target[2] and item[3] > target[3]:
        result += 1
print(result)
