def check(x, y, w):
    global minus_one, zero, plus_one
    check_num = graph[x][y]
    for i in range(x, x + w):
        for j in range(y, y + w):
            if graph[i][j] != check_num:
                nw = w // 3
                for a in range(3):
                    for b in range(3):
                        check(x + a * nw, y + b * nw, nw)
            else:
                if check_num == -1:
                    minus_one += 1
                elif check_num == 0:
                    zero += 1
                else:
                    plus_one += 1


if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    minus_one = 0
    zero = 0
    plus_one = 0
    check(0, 0, n)
    print(minus_one, zero, plus_one)

