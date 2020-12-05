class Board(object):
    ROWS = COLS = 720
    def __init__(self):
        self.board = self._create_empty_board()

    def clear(self):
        self.board = self._create_empty_board()
    
    def get_board(self):
        return self.board

    def update(self, x: int, y: int, color: tuple):
        self.board[x][y] = color

    def fill(self, x: int, y: int, color: tuple):
        pass

    def _create_empty_board(self):
        return [[(255, 255, 255) for _ in range(self.ROWS)] for _ in range(self.COLS)]
