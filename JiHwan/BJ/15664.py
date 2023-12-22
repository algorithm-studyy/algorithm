def back(start):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    prev = 0
    for i in range(start, n):
        if not visited[i] and prev != nums[i]:
            visited[i] = True
            answer.append(nums[i])
            prev = nums[i]
            back(i + 1)
            visited[i] = False
            answer.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    answer = []
    visited = [False] * n
    back(0)