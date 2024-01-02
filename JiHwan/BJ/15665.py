def back(start):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    prev = 0
    for i in range(n):
        if prev != nums[i]:
            answer.append(nums[i])
            prev = nums[i]
            back()
            answer.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    answer = []
    back(0)