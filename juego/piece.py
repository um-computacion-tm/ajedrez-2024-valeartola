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
    
    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        possible_positions = self.get_possible_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def possible_diagonal_positions(self, from_row, from_col):
        return (
            self.diag_possible_positions(from_row, from_col, 1, 1) +  # diagonal descendente derecha
            self.diag_possible_positions(from_row, from_col, -1, 1) +  # diagonal ascendente derecha
            self.diag_possible_positions(from_row, from_col, 1, -1) +  # diagonal descendente izquierda
            self.diag_possible_positions(from_row, from_col, -1, -1)  # diagonal ascendente izquierda
        )
    
    def possible_diagonal_positions(self, row, col, row_step, col_step):
        possibles = []
        next_row, next_col = row + row_step, col + col_step
        while 0 <= next_row < 8 and 0 <= next_col < 8:  # Dentro del tablero
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))  # Puede capturar
                break  # Detener si hay pieza, aliada o enemiga
            possibles.append((next_row, next_col))  # Añadir posición vacía
            next_row += row_step  # Seguir en la misma dirección
            next_col += col_step

        return possibles


    def possible_orthogonal_positions(self, from_row, from_col):
        return (
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col)
        )

    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            possibles.append((next_row, col))
        return possibles
