if __name__ == "__main__":
    n = int(input())
    count = 0
    for i in range(n):
        s, w = list(map(int, input().split()))
        back(s, w)

    print(count)