from sys import stdin


def get_two_input():
    a, b = map(int, stdin.readline().split(" "))
    return a, b


def dfs(a, b):
    if b == m:
        print(' '.join(nums))
        return
    for i in range(a, n + 1):
        nums[b] = str(i)
        dfs(i, b + 1)


if __name__ == '__main__':
    n, m = get_two_input()
    nums = ['0' for _ in range(m)]
    dfs(1, 0)
