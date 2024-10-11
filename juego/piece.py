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
    
    def _is_path_clear(self, from_row, from_col, to_row, to_col):
        """Verifica si el camino está despejado para movimientos rectos o diagonales."""
        if self._is_straight_move(from_row, from_col, to_row, to_col):
            return self._is_path_clear_straight(from_row, from_col, to_row, to_col)
        elif self._is_diagonal_move(from_row, from_col, to_row, to_col):
            return self._is_path_clear_diagonal(from_row, from_col, to_row, to_col)
        return False

    def _is_straight_move(self, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento es recto (horizontal o vertical)."""
        return from_row == to_row or from_col == to_col

    def _is_diagonal_move(self, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento es diagonal."""
        return abs(from_row - to_row) == abs(from_col - to_col)

    def _is_path_clear_straight(self, from_row, from_col, to_row, to_col):
        """Chequea si el camino está despejado para movimientos rectos (vertical u horizontal)."""
        
        # Calcular las diferencias entre filas y columnas
        row_diff = to_row - from_row
        col_diff = to_col - from_col

        # Verificar si es un movimiento recto (vertical u horizontal)
        if row_diff != 0 and col_diff != 0:
            return False  # No es un movimiento recto

        # Calcular los pasos en fila y columna
        step_row = (row_diff // abs(row_diff)) if row_diff != 0 else 0
        step_col = (col_diff // abs(col_diff)) if col_diff != 0 else 0
        distance = max(abs(row_diff), abs(col_diff))  # Usar la distancia máxima (en fila o columna)

        # Verificar si el camino está despejado
        for step in range(1, distance):
            current_row = from_row + step * step_row
            current_col = from_col + step * step_col
            if self.__board__.get_piece(current_row, current_col) is not None:
                return False  # Hay una pieza bloqueando el camino

        return True  # Camino despejado



    def _is_path_clear_diagonal(self, from_row, from_col, to_row, to_col):
        """Chequea si el camino está despejado para movimientos diagonales."""
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        row, col = from_row + row_step, from_col + col_step
        while row != to_row and col != to_col:
            if self.__board__.get_piece(row, col) is not None:
                return False
            row += row_step
            col += col_step
        return True
