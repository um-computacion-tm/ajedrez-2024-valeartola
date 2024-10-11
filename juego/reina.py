from juego.piece import Piece

class Reina(Piece):

    white_str  = "♕"
    black_str  = "♛"

    def valid_move(self, from_row, from_col, to_row, to_col):
        return self._is_path_clear(from_row, from_col, to_row, to_col)