P = int(input())
for k in range(P):
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                cnt += 1
    print(k + 1, cnt)