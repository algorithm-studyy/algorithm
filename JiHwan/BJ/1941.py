from collections import deque

def dfs_2(visited, r, c):


def dfs(depth, start, countY):
    global result
    global check
    global count_temp

    if countY >= 4:
        return
    if depth == 7:
        visited = [[1] * 5 for _ in range(5)]

        for i in arr:
            visited[i[0]][i[1]] = 0
        dfs_2(visited, arr[0][0], arr[0][1])
        if check:
            result += 1
            check = False
        count_temp = 0
        return


if __name__ == "__main__":
    students = [list(input()) for _ in range(5)]
    result = 0
    check = False
    count_temp = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    dfs(0, 0, 0)
    print(result)
