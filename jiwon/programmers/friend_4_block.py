# 1. 4블록이 있는지 확인
# 2. 4블록이 있으면 다른 걸로 채움 ex) 0
# 3. 0으로 채워져 있으면 맨 아래 0인 것과 swap
# 4. 1, 2, 3 반복

class FriendsBlock:
    def __init__(self, board, m, n):
        self.m = m
        self.n = n
        self.board = [list(row) for row in board]
        self.remove_blocks = set()
        self.dx = [1, 0, 1]
        self.dy = [0, 1, 1]

    def get_remove_blocks_count(self):
        return len(self.remove_blocks)

    def reset_remove_blocks(self):
        self.remove_blocks = set()

    def append_remove_blocks(self, x, y):
        remove_list = [(y, x)]
        for i in range(3):
            nx, ny = x + self.dx[i], y + self.dy[i]
            remove_list.append((ny, nx))
        self.remove_blocks.update(tuple(remove_list))

    def is_4block(self, x, y):
        c = self.board[y][x]
        for i in range(3):
            nx, ny = x + self.dx[i], y + self.dy[i]
            if self.board[ny][nx] != c:
                return False
        return True

    def get_remove_blocks(self):
        self.reset_remove_blocks()
        for y in range(self.m - 1):
            for x in range(self.n - 1):
                if self.board[y][x] == 0 or not self.is_4block(x, y):
                    continue
                self.append_remove_blocks(x, y)

    def change_board_using_remove_blocks(self):
        for y, x in self.remove_blocks:
            self.board[y][x] = 0

    def down_blocks(self):
        for y in range(self.m - 1, -1, -1):
            for x in range(self.n):
                if self.board[y][x] == 0:
                    self.swap(x, y)

    def swap(self, x, y):
        ny, nx = self.find_not_zero_on_vertical_line(x, y)
        if ny == y and nx == x:
            return
        self.board[ny][nx], self.board[y][x] = self.board[y][x], self.board[ny][nx]

    def find_not_zero_on_vertical_line(self, x, y):
        for ny in range(y - 1, -1, -1):
            if self.board[ny][x] != 0:
                return ny, x
        return y, x


def solution(m, n, board):
    answer = 0
    friend_block = FriendsBlock(board, m, n)
    while True:
        friend_block.get_remove_blocks()
        if not friend_block.get_remove_blocks_count():
            break
        answer += friend_block.get_remove_blocks_count()
        friend_block.change_board_using_remove_blocks()
        friend_block.down_blocks()
    return answer