n = int(input())
t = int(input())
k = int(input())

b = d = 0
arr = []
count = 0
while True:
    count += 1

    for i in range(2):
        b += 1
        arr.append((b, 0))
        d += 1
        arr.append((d, 1))
    for i in range(count+1):
        b += 1
        arr.append((b, 0))
    for i in range(count + 1):
        d += 1
        arr.append((d, 1))

    if b >= t:
        print(arr.index((t, k)) % n)
        break

