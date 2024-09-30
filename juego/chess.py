from juego.board import Board
from juego.exceptions import EmptyPosition
from juego.exceptions import InvalidTurn
from juego.exceptions import InvalidMove
from juego.exceptions import InvalidMoveSameColor
from juego.exceptions import InvalidCoordinate
from juego.exceptions import InvalidSamePlace

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "BLANCO"

    def is_playing(self):
        return True
    
    def move(self, from_row, from_col, to_row, to_col):
        if not self.__board__.is_valid_coordinate(from_row, from_col) or not self.__board__.is_valid_coordinate(to_row, to_col):
            raise InvalidCoordinate        
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece: 
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.valid_move(from_row, from_col, to_row, to_col):#Sin Test DUDA
            raise InvalidMove()
        if from_row == to_row and from_col == to_col:
            raise InvalidSamePlace
        target_piece = self.__board__.get_piece(to_row, to_col)
        if target_piece is not None and target_piece.get_color() == piece.get_color():
            raise InvalidMoveSameColor()
        self.__board__.move(from_row, from_col, to_row, to_col)#Sin Test
        self.change_turn()#Sin Test
        
    @property  
    def turn(self):
            return self.__turn__

    def show_board(self):
         return str(self.__board__)   

    def change_turn(self):
        if self.__turn__ == "BLANCO":
            self.__turn__ = "NEGRO"
        else:
            self.__turn__ = "BLANCO"      

    

