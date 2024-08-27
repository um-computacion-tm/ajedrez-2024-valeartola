from juego.piece import Piece

class Torre(Piece):
    white_str  = "♖"
    black_str  = "♜"

    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row +1, 8): #range(inicio, fin que no esta incluido)
            possibles.append((next_row, col))
        return possibles
    
    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row -1, -1, -1): #range(inicio, fin que no esta incluido)
            possibles.append((next_row, col))
        return possibles    
    

