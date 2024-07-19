def change(idx):
    if light[idx] == 0:
        light[idx] = 1
    else:
        light[idx] = 0


n = int(input())

light = list(map(int, input().split()))
st_num = int(input())

for st in range(st_num):
    gen, num = map(int, input().split())

    if gen == 1:
        for i in range(1, n + 1):
            if i % num == 0:
                change(i - 1)
    else:
        idx = num - 1
        i = 1
        change(idx)
        while num - i >= 1 and num + i <= n:
            if light[idx - i] == light[idx + i]:
                change(idx - i)
                change(idx + i)
            else:
                break
            i += 1
print(*light)
