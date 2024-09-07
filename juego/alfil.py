from juego.piece import Piece

class Alfil(Piece):

    white_str  = "♗"
    black_str  = "♝"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.possible_positions_diagonal(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions

    def possible_positions(self, row, col):
        possibles = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for next_row, next_col in directions:
            possibles.extend(self._explore_diagonal(row, col, next_row, next_col))
        return possibles

    def _explore_diagonal(self, row, col, next_row, next_col):
        possibles = []
        while True:
            row += next_row
            col += next_col
            if not (0 <= row < 8 and 0 <= col < 8):  # fuera de los límites del tablero
                break
            other_piece = self.__board__.get_piece(row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, col))
                break
            possibles.append((row, col))
        return possibles  


