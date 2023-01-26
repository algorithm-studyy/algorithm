from sys import stdin


def get_two_input():
    a, b = map(int, stdin.readline().split(" "))
    return a, b


def dfs(b):
    if b == m:
        print(' '.join(nums))
    else:
        for i in range(1, n + 1):
            if checks[i]:
                continue
            nums[b] = str(i)
            checks[i] = True
            dfs(b + 1)
            checks[i] = False


if __name__ == '__main__':
    n, m = get_two_input()
    nums = ['0' for _ in range(m)]
    checks = [False for _ in range(n + 1)]
    dfs(0)

