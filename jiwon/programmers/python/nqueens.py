# Queen의 이동 방향에 있을 시 시작 안하기

answer = 0


def dfs(d, n, arr):
    global answer
    if d == n:
        answer += 1
        return
    r = arr[-1][0] if arr else 0
    c = arr[-1][1] if arr else 0
    for i in range(r, n):
        for j in range(c, n):
            if not can_attack(arr, j, i, n):
                arr.append((i, j))
                print(r, c, i, j, arr)
                dfs(d + 1, n, arr)
                arr.pop()


def can_attack(arr, x, y, n):
    if not arr:
        return False
    for py, px in arr:
        if py == y or px == x:
            return True
    for dy, dx in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
        for k in range(1, 12):
            nx, ny = x + dx * k, y + dy * k
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            for py, px, in arr:
                if py == ny and px == nx:
                    return True
    return False


def solution(n):
    dfs(0, n, [])
    return answer
