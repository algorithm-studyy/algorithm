from sys import stdin


def get_two_input():
    a, b = map(int, stdin.readline().split(" "))
    return a, b


def dfs(b):
    if b == m:
        print(' '.join(print_nums))
        return
    for i in range(len(nums)):
        if b > 0 and int(print_nums[b - 1]) > nums[i]:
            continue
        print_nums[b] = str(nums[i])
        dfs(b + 1)


if __name__ == '__main__':
    n, m = get_two_input()
    nums = list(map(int, stdin.readline().split(" ")))
    nums.sort()
    print_nums = ['0' for _ in range(m)]
    dfs(0)
