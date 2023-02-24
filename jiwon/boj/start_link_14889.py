from sys import stdin
from sys import maxsize

answer = maxsize


def sum_list(lst):
    val = 0
    for i, value in enumerate(lst):
        for j in range(i + 1, len(lst)):
            val += s_list[value][lst[j]]
            val += s_list[lst[j]][value]
    return val


def dfs(d, a, link):
    global answer
    if d == n2:
        start = [i for i in range(n) if i not in link]
        link_sum = sum_list(link)
        start_sum = sum_list(start)
        answer = min(abs(start_sum - link_sum), answer)
        return
    for i in range(a, n):
        link.append(i)
        dfs(d + 1, i + 1, link)
        link.pop()


if __name__ == '__main__':
    n = int(stdin.readline())
    n2 = n // 2
    s_list = [list(map(int, stdin.readline().strip().split(" "))) for _ in range(n)]
    s_sum = sum([sum(i) for i in s_list])
    dfs(0, 0, [])
    print(answer)
