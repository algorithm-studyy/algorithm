n, s = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
limit = 1<<n

for i in range(1, limit):
    total = 0
    for j in range(n):
        if i & (1<<j):
            total +=arr[j]
    if total == s:
        answer +=1

print(answer)

