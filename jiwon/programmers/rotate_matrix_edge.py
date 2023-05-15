# 회전을 시킬 때 가장 작은 수 찾기


def solution(rows, columns, queries):
    answer = []
    b = [[i + (j * columns) + 1 for i in range(columns)] for j in range(rows)]
    for y1, x1, y2, x2 in queries:
        y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1
        val = b[y1][x1]
        next_val = 0
        result = 1e9
        for i in range(x1, x2):
            next_val, b[y1][i + 1] = b[y1][i + 1], val
            val, result = next_val, min(result, val)
        for i in range(y1, y2):
            next_val, b[i + 1][x2] = b[i + 1][x2], val
            val, result = next_val, min(result, val)
        for i in range(x2, x1, -1):
            next_val, b[y2][i - 1] = b[y2][i - 1], val
            val, result = next_val, min(result, val)
        for i in range(y2, y1, -1):
            next_val, b[i - 1][x1] = b[i - 1][x1], val
            val, result = next_val, min(result, val)
        answer.append(result)
    return answer
