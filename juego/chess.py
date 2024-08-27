from juego.board import Board
class InvalidMoveError(Exception):
     pass

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "BLANCO"

    def is_valid_coordiante(self, row, col):
        return 0 <= row <= 8 and 0 <= col <= 8
    
    def move(self, from_row, from_col, to_row, to_col):
            if not self.is_valid_coordinate(from_row, from_col) or not self.is_validate_coordinate(to_row, to_col): 
                raise InvalidMoveError
            piece = self.board.get_piece(from_row, from_col)
            self.change_turn()
            
    @property  
    def turn(self):
            return self.__turn__

    def show_board(self):
         return str(self.__board__)   

    def change_turn(self):
        if self.__turn__ == "BLANCO":
            self.__turn__ == "NEGRO"
        else:
            self.__turn__ == "BLANCO"      

    

