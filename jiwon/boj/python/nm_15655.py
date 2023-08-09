from sys import stdin


def get_two_input():
    a, b = map(int, stdin.readline().split(" "))
    return a, b


def dfs(a, b):
    if b == m:
        print(' '.join(print_nums))
        return
    for i in range(a, len(nums)):
        if checks[i]:
            continue
        checks[i] = True
        print_nums[b] = str(nums[i])
        dfs(i + 1, b + 1)
        checks[i] = False


if __name__ == '__main__':
    n, m = get_two_input()
    nums = list(map(int, stdin.readline().split(" ")))
    nums.sort()
    print_nums = ['0' for _ in range(m)]
    checks = [False for _ in range(n)]
    dfs(0, 0)
