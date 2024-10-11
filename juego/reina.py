from juego.piece import Piece

class Reina(Piece):

    white_str  = "♕"
    black_str  = "♛"

    def valid_move(self, from_row, from_col, to_row, to_col):
        # Movimiento como torre (horizontal o vertical)
        # if from_col == to_col or from_row == to_row: 
        #     # Validación para movimiento horizontal o vertical
        #     if self._is_path_clear_straight(from_row, from_col, to_row, to_col):
        #         return True

        # # Movimiento como alfil (diagonal)
        # if abs(from_row - to_row) == abs(from_col - to_col):
        #     # Validación para movimiento diagonal
        #     if self._is_path_clear_diagonal(from_row, from_col, to_row, to_col):
        #         return True 


        # # No es un movimiento válido para la reina
        # return False
        return self._is_path_clear(from_row, from_col, to_row, to_col)