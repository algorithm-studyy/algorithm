from sys import stdin

# if Max 6 or 9, max_val // 2
# else
arr = [0] * 10
room = list(map(int, list(stdin.readline().strip())))
for c in room:
    arr[c] += 1
max_idx, max_val = 0, 0
for idx, item in enumerate(arr):
    if idx != 9 and idx != 6 and item > max_val:
        max_idx = idx
        max_val = item
print(max((arr[9] + arr[6] + 1) // 2, max_val))

