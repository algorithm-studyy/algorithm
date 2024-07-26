n = int(input())

cost = list(map(int, input().split()))
max_cost = int(input())

total = 0
over_cost = []

if sum(cost) <= max_cost:
    print(max(cost))
else:
    average_cost = sum(cost) // len(cost)
    for c in cost:
        if c <= average_cost:
            total += c
        else:
            over_cost.append(c)
    answer = (max_cost - total) // len(over_cost)
    print(answer)
