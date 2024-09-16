if __name__ == "__main__":
    N = int(input())
    A = sorted(list(map(int, input().split())))
    M = int(input())
    B = list(map(int, input().split()))

    for b in B:
        lt, rt = 0, N - 1
        isExist = False

        while lt <= rt:
            mid = (lt + rt) // 2

            if A[mid] == b:
                isExist = True
                print(1)
                break
            elif A[mid] > b:
                rt = mid - 1
            else:
                lt = mid + 1
        if not isExist:
            print(0)