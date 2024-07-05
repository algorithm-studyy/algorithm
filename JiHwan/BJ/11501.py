T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    num = arr[0]
    total = 0

    for i in range(1, len(arr)):
        if num < arr[i]:
            num = arr[i]
        total = total + num - arr[i]

    print(total)
