from juego.piece import Piece

class Torre(Piece):
    
    white_str  = "♖"
    black_str  = "♜"

    def valid_move(self, from_row, from_col, to_row, to_col):
        # # Movimiento vertical
        # if from_col == to_col or from_row == to_row:
        #     # Si No hay piezas en el medio: true
        #     if  self._is_path_clear_straight(from_row, from_col, to_row, to_col):
        #         return True
        # return False  # No es un movimiento válido para la torre

        return self._is_straight_move(from_row, from_col, to_row, to_col) and \
               self._is_path_clear_straight(from_row, from_col, to_row, to_col)   