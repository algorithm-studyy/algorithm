import sys
from bisect import bisect_left

input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    li, dic = [], {}

    for i in range(N):
        x, y = input().split()
        li.append(int(y))
        dic[i] = x

    for _ in range(M):
        print(dic[bisect_left(li, int(input()))])
