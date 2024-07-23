n = int(input())
dis = list(map(int, input().split()))
cost = list(map(int, input().split()))

answer = cost[0] * dis[0]
a = cost[0]

for i in range(1, n - 1):
    if cost[i] < a:
        a = cost[i]
    answer += a * dis[i]

print(answer)
