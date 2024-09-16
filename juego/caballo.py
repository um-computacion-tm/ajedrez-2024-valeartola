from juego.piece import Piece

class Caballo(Piece):

    white_str  = "♘"
    black_str  = "♞"

    def get_possible_positions(self, from_row, from_col):
        return ()