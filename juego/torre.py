from juego.piece import Piece

class Torre(Piece):
    
    white_str  = "♖"
    black_str  = "♜"

    def valid_move(self, from_row, from_col, to_row, to_col):
        # Movimiento vertical
        if from_col == to_col or from_row == to_row:
            # Validación para movimiento horizontal o vertical
            if not self._is_path_clear_straight(from_row, from_col, to_row, to_col):
                return False
        return True  # No es un movimiento válido para la torre