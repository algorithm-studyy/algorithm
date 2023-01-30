from sys import stdin

answer = 0


def get_three_input():
    a, b, c = map(int, stdin.readline().split(" "))
    return a, b, c


def is_adjacency(i, j):
    wasd = [[1, 0], [-1, 0], [0, -1], [0, 1], [0, 0]]
    for p in prev:
        for d in wasd:
            if p[0] + d[0] == i and p[1] + d[1] == j:
                return True
    return False


def dfs(a, b, c, s):
    global answer
    if c == k:
        answer = s if answer < s else answer
        return
    for i in range(a, len(nums)):
        for j in range(b, len(nums[i])):
            if is_adjacency(i, j):
                continue
            prev.append([i, j])
            ab = a + b
            dfs(ab // n, ab % m, c + 1, nums[i][j] + s)
            prev.pop()


if __name__ == '__main__':
    n, m, k = get_three_input()
    nums = list(list(map(int, stdin.readline().split(" "))) for _ in range(n))
    prev = []
    dfs(0, 0, 0, 0)
    print(answer)
