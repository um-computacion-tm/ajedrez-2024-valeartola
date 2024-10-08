from juego.board import Board
from juego.exceptions import EmptyPosition
from juego.exceptions import InvalidTurn
from juego.exceptions import InvalidMove
from juego.exceptions import InvalidMoveSameColor
from juego.exceptions import InvalidCoordinate
from juego.exceptions import InvalidSamePlace
from juego.exceptions import Withoutcoordinate

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "BLANCO"
        self.__game_over__ = False
        self.__winner__ = " " 

    def is_playing(self):
        return not self.__game_over__
    
    def move(self, from_row, from_col, to_row, to_col):
        if not self.__board__.is_valid_coordinate(from_row, from_col) or not self.__board__.is_valid_coordinate(to_row, to_col):
            raise InvalidCoordinate        
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece: 
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        target_piece = self.__board__.get_piece(to_row, to_col)
        if from_row == to_row and from_col == to_col:
            raise InvalidSamePlace
        if target_piece is not None and target_piece.get_color() == piece.get_color():
            raise InvalidMoveSameColor()
        if not piece.valid_move(from_row, from_col, to_row, to_col):#Sin Test DUDA
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)#Sin Test
        self.change_turn()#Sin Test

        self.__draw_offered__ = False
        self.check_game_over()
        
    @property  
    def turn(self):
        return self.__turn__
    
    @property
    def winner(self):
        return self.__winner__

    def show_board(self):
         return str(self.__board__)   

    def change_turn(self):
        if self.__turn__ == "BLANCO":
            self.__turn__ = "NEGRO"
        else:
            self.__turn__ = "BLANCO"      

    def check_game_over(self):
        # Revisa si uno de los jugadores se ha quedado sin piezas
        white_count, black_count = self.count_pieces()
        if white_count == 0:
            self.__game_over__ = True
            self.__winner__ = "NEGRO"
        elif black_count == 0:
            self.__game_over__ = True
            self.__winner__ = "BLANCO"

    def count_pieces(self):
        # Cuenta las piezas de cada jugador en el tablero
        white_count = 0
        black_count = 0
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if piece:
                    if piece.get_color() == "BLANCO":
                        white_count += 1
                    elif piece.get_color() == "NEGRO":
                        black_count += 1
        return white_count, black_count
    
    def draw(self):
            self.__game_over__ = True
            self.__winner__ = "Ninguno"
            

    

    

