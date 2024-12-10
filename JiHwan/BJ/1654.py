if __name__ == "__main__":
    # 입력값
    K, N = map(int, input().split())
    arr = []
    for _ in range(K):
        arr.append(int(input()))

    left, right = 1, max(arr)
    while left <= right:
        mid = (left + right) // 2
        lan = 0
        for i in arr:
            lan += i // mid

        if lan >= N:
            left = mid + 1
        else:
            right = mid - 1

    print(right)