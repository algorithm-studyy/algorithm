if __name__ == "__main__":
    M, N = map(int, input().split())
    L = sorted(list(map(int, input().split())))
    start = 1
    end = max(L)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for l in L:
            if l < mid:
                continue
            else:
                cnt += l // mid
        if cnt >= M:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    print(answer)


