if __name__ == "__main__":
    N = int(input())
    budget_list = list(map(int, input().split()))
    max_budget = int(input())
    answer = 0
    start, end = 1, max(budget_list)

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for budget in budget_list:
            if budget > mid:
                total += mid
            else:
                total += budget
        if total <= max_budget:
            answer = mid
            start = mid + 1
        else:
            end -= 1
    print(answer)