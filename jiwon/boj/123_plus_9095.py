from sys import stdin

answer = 0


def dfs(d):
    global answer
    if d >= a:
        if a == d:
            answer += 1
        return
    dfs(d + 1)
    dfs(d + 2)
    dfs(d + 3)


if __name__ == '__main__':
    n = int(stdin.readline())
    for _ in range(n):
        answer = 0
        a = int(stdin.readline())
        dfs(0)
        print(answer)
