import sys

N = int(sys.stdin.readline())
arr = []
stack = [0 for _ in range(N)]
for i in range(N):
    arr.append(int(input()))
arr.sort()

stack[0] = arr[0] + arr[1]

for i in range(1, N-1):
    stack[i] = stack[i-1]+arr[i+1]
print(sum(stack))


