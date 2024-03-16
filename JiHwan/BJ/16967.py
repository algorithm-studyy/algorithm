import sys
h, w, x, y = list(map(int, sys.stdin.readline().split()))

b = [0 * (w + y) for _ in range(h + x)]

for i in range(h + x):
    b[i] = list(map(int, sys.stdin.readline().split()))

