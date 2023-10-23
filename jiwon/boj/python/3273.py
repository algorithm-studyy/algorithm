from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
x = int(stdin.readline())
arr.sort()
answer = 0

start = 0
end = n - 1
while start < end:
    num = arr[start] + arr[end]
    if num > x:
        end -= 1
    elif num < x:
        start += 1
    else:
        answer += 1
        end -= 1
print(answer)
