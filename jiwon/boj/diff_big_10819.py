from sys import stdin

answer = 0


def sum_diff(lst):
    result = [abs(lst[i] - lst[i + 1]) for i in range(len(lst) - 1)]
    return sum(result)


def dfs(a, s):
    global answer
    if a == m:
        val = sum_diff(s)
        answer = val if answer < val else answer
        return
    for i in range(m):
        if checks[i]:
            continue
        checks[i] = True
        s.append(nums[i])
        dfs(a + 1, s)
        checks[i] = False
        s.pop()


def get_line_input():
    n = int(stdin.readline())
    line = list(map(int, stdin.readline().strip().split(' ')))
    return n, line


if __name__ == '__main__':
    m, nums = get_line_input()
    checks = [False for _ in range(m)]
    dfs(0, [])
    print(answer)
