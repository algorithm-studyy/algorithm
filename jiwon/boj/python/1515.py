def solution():
    n = list(input().strip())
    cur = int(n[0])
    for i, item in enumerate(n):
        cur += 1
        while True:
            if item in str(cur):
                break
            cur += 1

    print(cur)


solution()
