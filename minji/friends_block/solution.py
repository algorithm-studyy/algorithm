import numpy as np

def find_delete_block(m, n, board, map):
    for row in range(m-1):
        for col in range(n-1):
            char = board[row][col]
            char_next = board[row][col+1]
            char_under = board[row+1][col]
            char_diagonal = board[row+1][col+1]
            if char == '0':
                map[row][col] = -1
                continue
            if char == char_next and char == char_under and char == char_diagonal:
                map[row][col] = 0
                map[row+1][col] = 0
                map[row+1][col+1] = 0
                map[row][col+1] = 0
    return map

# TODO: MAP 이용할 다른 방법 다시 생각해보기
# TODO: 지워진 블록과 이제 지워야할 블록 구분방법 생각해보기
def down_block(n, board, map):
    board = board.T
    map_t = map.T
    
    for col in range(n):
        map_info = map[:, col]
        index_list = np.where(map_info == 0)[0]
        board[col][index_list] = 0
        map_t[col][index_list] = -1
        board[col] = board[col][map_info.argsort()]
        map_t[col] = map_t[col][map_info.argsort()] 
    
    map = map_t.T
    board = board.T
    return board, map

def solution(m, n, board):
    answer = 0
    board_test = list()
    for string in board:
        board_test.append([c for c in string])
    board_test = np.array(board_test)
    map = np.ones((m,n))
    while True:
        map = find_delete_block(m, n, board_test, map)
        count = len(np.where(map == 0)[0])
        if count == 0:
            break
        answer += count
        board, map = down_block(n, board_test, map)
    
    return answer