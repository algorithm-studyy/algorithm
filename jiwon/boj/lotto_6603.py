from sys import stdin


answer = []


def dfs(a, b):
    global answer
    if a == 6:
        answer.append(' '.join(list(map(str, print_nums))))
        return
    for i in range(b, n):
        print_nums[a] = nums[i]
        dfs(a + 1, i + 1)


if __name__ == '__main__':
    while True:
        k = stdin.readline().strip().split(' ')
        if k[0] == '0':
            break
        n, nums = int(k[0]), list(map(int, k[1:]))
        print_nums = [0 for _ in range(6)]
        dfs(0, 0)
        answer[-1] += '\n'
    answer[-1] = answer[-1].strip()
    print('\n'.join(answer), end='')

