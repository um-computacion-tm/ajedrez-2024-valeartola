from juego.piece import Piece

class Reina(Piece):

    white_str  = "♕"
    black_str  = "♛"


    def valid_positions(self,from_row, from_col, to_row, to_col):
        possible_positions = (self.possible_positions_hr(from_row, from_col) + self.possible_positions_hl(from_row, from_col) + 
                            self.possible_positions_vd(from_row, from_col) + self.possible_positions_va(from_row, from_col))
        return (to_row, to_col) in possible_positions
    
    def possible_positions_vd(self,row,col):
        possibles = []
        for next_row in range (row + 1, 8):
            possibles.append((next_row,col))
        return possibles

    def possible_positions_va(self,row,col):
        possibles = []
        for next_row in range (row - 1, -1, -1):
            possibles.append((next_row,col))
        return possibles


"""    def get_possible_positions(self, from_row, from_col):
        return self.possible_orthogonal_positions(
            from_row,
            from_col,
        ) + self.possible_diagonal_positions(
            from_row,
            from_col,
        )"""