def solution():
    n, x = map(int, input().split())
    visits = list(map(int, input().split()))
    visit = sum(visits[:x])
    result = dict()
    result[visit] = 1
    for i in range(n - x):
        visit += visits[i + x] - visits[i]
        result[visit] = result.get(visit, 0) + 1
    max_visit = max(result.keys())
    if max_visit == 0:
        print("SAD")
    else:
        print(max_visit)
        print(result[max_visit])


solution()
