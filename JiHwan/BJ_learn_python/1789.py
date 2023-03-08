import sys

S = int(sys.stdin.readline())
total = 0
count = 0

while True:
    count += 1
    total += count
    if total > S:
        break
print(count-1)