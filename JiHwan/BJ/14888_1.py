def dfs(depth, num):
    global answer, operator

    if depth == n - 1:
        answer.append(num)

    if operator[0] != 0:
        operator[0] -= 1
        dfs(depth + 1, num + a[depth + 1])
        operator[0] += 1
    if operator[1] != 0:
        operator[1] -= 1
        dfs(depth + 1, num - a[depth + 1])
        operator[1] += 1
    if operator[2] != 0:
        operator[2] -= 1
        dfs(depth + 1, num * a[depth + 1])
        operator[2] += 1
    if operator[3] != 0:
        operator[3] -= 1
        dfs(depth + 1, int(num / a[depth + 1]))
        operator[3] += 1


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    answer = []
    dfs(0, a[0])

    print(max(answer))
    print(min(answer))