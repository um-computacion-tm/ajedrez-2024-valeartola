from juego.piece import Piece

class Peon(Piece):

    white_str  = "♙"
    black_str  = "♟"

    def valid_move(self, from_row, from_col, to_row, to_col):
        # Movimiento básico del peón
        direction = 1 if self.__color__ == "BLANCO" else -1
        # Verificar si está en la posición inicial
        starting_row = 6 if self.__color__ == "NEGRO" else 1

        # Mover hacia adelante (1 o 2 casillas si está en la posición inicial)
        if from_col == to_col:
            if (from_row + direction) == to_row:
                return True
            # Movimiento de 2 casillas si está en la posición inicial
            if from_row == starting_row and (from_row + 2 * direction) == to_row:
                return True

        # Captura en diagonal
        if abs(from_col - to_col) == 1 and (from_row + direction) == to_row and self.__board__.get_piece(to_row, to_col):
            return True

        return False