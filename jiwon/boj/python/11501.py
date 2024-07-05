from sys import stdin


def solution():
    for _ in range(int(stdin.readline())):
        n = int(stdin.readline())
        stocks = list(map(int, stdin.readline().split()))[::-1]
        result = 0
        num = stocks[0]
        for i in range(1, n):
            num = max(num, stocks[i])
            result += num - stocks[i]
        print(result)


solution()
