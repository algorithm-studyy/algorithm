from sys import stdin


def get_line_input():
    n = int(stdin.readline())
    line = stdin.readline().strip().split(" ")
    return n, line


def dfs(a, answer):
    if a == k + 1:
        answers.append(''.join(list(map(str, answer))))
        return
    for i in range(9, -1, -1):
        if a > 0:
            if nums[i]:
                continue
            elif sign[a - 1] == '>' and answer[a - 1] < i:
                continue
            elif sign[a - 1] == '<' and answer[a - 1] > i:
                continue

        nums[i] = True
        answer.append(i)
        dfs(a + 1, answer)
        answer.pop()
        nums[i] = False


if __name__ == '__main__':
    k, sign = get_line_input()
    nums = [False for _ in range(10)]
    answers = []
    dfs(0, [])
    print(answers[0], answers[-1], sep='\n')
