def create_col_stack(board):
    return list(map(lambda i: list(filter(lambda x: x != 0, [row[i] for row in board]))[::-1], range(len(board))))


def solution(board, moves):
    answer = 0
    result = create_col_stack(board)
    stack = []
    for move in moves:
        if not result[move - 1]:
            continue
        next_value = result[move - 1].pop()
        if stack and stack[-1] == next_value:
            stack.pop()
            answer += 2
        else:
            stack.append(next_value)
    return answer
