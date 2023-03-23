import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_sorted = sorted(rank)
    top = 0
    result = 1

    for i in range(1, len(rank_sorted)):
        if rank_sorted[i][1] < rank_sorted[top][1]:
            top = i
            result += 1

    print(result)
