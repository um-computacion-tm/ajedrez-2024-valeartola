from juego.piece import Piece

class Caballo(Piece):

    white_str  = "♘"
    black_str  = "♞"

    def valid_move(self, from_row, from_col, to_row, to_col):    
        return (abs(from_row - to_row), abs(from_col - to_col)) in [(2, 1), (1, 2)]

