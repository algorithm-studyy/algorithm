import sys
import heapq

if __name__ == "__main__":
    n = int(input())
    answer = []
    for _ in range(n):
        x = int(sys.stdin.readline())

        if x != 0:
            heapq.heappush(answer, x)
        else:
            if len(answer) != 0:
                print(heapq.heappop(answer))
            else:
                print(0)