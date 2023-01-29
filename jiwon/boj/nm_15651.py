from sys import stdin


def get_two_input():
    a, b = map(int, stdin.readline().split(" "))
    return a, b


def dfs(b):
    if b == m:
        print(' '.join(nums))
        return
    for i in range(1, n + 1):
        nums[b] = str(i)
        dfs(b + 1)


if __name__ == '__main__':
    n, m = get_two_input()
    nums = ['0' for _ in range(m)]
    dfs(0)
