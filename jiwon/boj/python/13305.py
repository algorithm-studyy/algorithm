def solution():
    n = int(input())
    city = list(map(int, input().split()))
    gs = list(map(int, input().split()))
    cost = city[0] * gs[0]
    min_gas = gs[0]
    for i in range(1, n - 1):
        min_gas = min(min_gas, gs[i])
        cost += city[i] * min_gas
    print(cost)


solution()
