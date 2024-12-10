def cal_answer(ans):
    real_ans = ans.replace(' ', '')
    if eval(real_ans) == 0:
        print(real_ans)


def dfs(depth, num):
    if depth == n + 1:
        return cal_answer(num)

    dfs(depth + 1, num + ' ' + str(depth))
    dfs(depth + 1, num + '+' + str(depth))
    dfs(depth + 1, num + '-' + str(depth))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        dfs(2, '1')