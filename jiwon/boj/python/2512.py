def solution():
    n = int(input())
    budgets = list(map(int, input().split()))
    total = int(input())
    left, right = 0, max(budgets)
    while left <= right:
        mid = (left + right) // 2
        new_total = 0
        for budget in budgets:
            new_total += budget if budget < mid else mid
        if new_total <= total:
            left = mid + 1
        else:
            right = mid - 1
    print(right)


solution()
