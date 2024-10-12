from juego.piece import Piece

class Alfil(Piece):

    white_str  = "♗"
    black_str  = "♝"

    def valid_move(self, from_row, from_col, to_row, to_col):
        if not self._is_diagonal_move(from_row, from_col, to_row, to_col):
            return False
        
        if not self._is_path_clear_diagonal(from_row, from_col, to_row, to_col):
            return False
        
        return True