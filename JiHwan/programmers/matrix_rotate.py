def solution(rows, columns, queries):
    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    i = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = i
            i += 1

    for x1, y1, x2, y2 in queries:
        print(x1, y1, x2, y2)
        tmp = array[x1 - 1][y1 - 1]
        mini = tmp
    return answer