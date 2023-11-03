from sys import stdin


def get_two_input():
    a, b = map(int,stdin.readline().split(" "))
    return a, b


def dfs(a, b):
    if b == m:
        print(' '.join(nums))
        return
    for i in range(a, n + 1):
        if checks[i]:
            continue
        checks[i] = True
        nums[b] = str(i)
        dfs(i + 1, b + 1)
        checks[i] = False


if __name__ == '__main__':
    n, m = get_two_input()
    nums = ['0' for _ in range(m)]
    checks = [False for _ in range(n + 1)]
    dfs(1, 0)
