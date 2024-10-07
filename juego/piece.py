class Piece():
    def __init__(self,color, board):
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        if self.__color__ == "BLANCO":
            return self.white_str
        else:
            return self.black_str

    def get_color(self):
        return self.__color__

    def _is_path_clear_straight(self, from_row, from_col, to_row, to_col):
        # Movimiento vertical
        if from_col == to_col:
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if self.__board__.get_piece(row, from_col) is not None: #Sin Test
                    return False  # Hay una pieza bloqueando el camino

        # Movimiento horizontal
        elif from_row == to_row:
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if self.__board__.get_piece(from_row, col) is not None:
                    return False  # Hay una pieza bloqueando el camino

        # No se encontró ninguna pieza bloqueando el camino
        return True

    def _is_path_clear_diagonal(self, from_row, from_col, to_row, to_col):
        # Movimiento diagonal
        row_step = 1 if to_row > from_row else -1 #Sin Test 
        col_step = 1 if to_col > from_col else -1
        row, col = from_row + row_step, from_col + col_step
        while row != to_row and col != to_col:
            if self.__board__.get_piece(row, col) is not None:
                return False  # Hay una pieza bloqueando el camino
            row += row_step
            col += col_step

        # No se encontró ninguna pieza bloqueando el camino
        return True