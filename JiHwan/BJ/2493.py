import sys

n = int(input())
m = list(map(int, sys.stdin.readline().split()))

answer = [0] * n
stack = []

for i in range(len(m)):
    while stack:
        if m[stack[-1][0]] < m[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0] + 1
            break
    stack.append((i, m[i]))

print(* answer)



