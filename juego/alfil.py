from juego.piece import Piece

class Alfil(Piece):

    white_str  = "♗"
    black_str  = "♝"

    def valid_move(self, from_row, from_col, to_row, to_col):
        # # Movimiento en diagonal
        # if abs(from_row - to_row) == abs(from_col - to_col):
        #     if self._is_path_clear_diagonal(from_row, from_col, to_row, to_col):
        #        return True
        # return False  # No es un movimiento válido para el alfil
        return self._is_diagonal_move(from_row, from_col, to_row, to_col) and \
               self._is_path_clear_diagonal(from_row, from_col, to_row, to_col)