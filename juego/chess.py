from juego.board import Board
from juego.exceptions import EmptyPosition
from juego.exceptions import InvalidTurn
from juego.exceptions import InvalidMove

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "BLANCO"

    def is_playing(self):
        return True

    def is_valid_coordiante(self, row, col):
        return 0 <= row <= 8 and 0 <= col <= 8
    
    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
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

    

