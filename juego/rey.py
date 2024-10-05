from juego.piece import Piece

class Rey(Piece):

    white_str  = "♔"
    black_str  = "♚"
     
    def valid_move(self, from_row, from_col, to_row, to_col):
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1