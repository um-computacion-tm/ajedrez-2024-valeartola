from juego.torre import Torre
from juego.caballo import Caballo
from juego.alfil import Alfil
from juego.reina import Reina
from juego.rey import Rey
from juego.peon import Peon
from juego.exceptions import OutOfBoard


class Board():
    def __init__(self, for_test = False):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:
            self.__positions__[0][0] = Torre("BLANCO", self) 
            self.__positions__[0][7] = Torre("BLANCO", self)         
            self.__positions__[7][7] = Torre("NEGRO", self)      
            self.__positions__[7][0] = Torre("NEGRO", self)  
            self.__positions__[0][1] = Caballo("BLANCO", self)
            self.__positions__[0][6] = Caballo("BLANCO", self)        
            self.__positions__[7][6] = Caballo("NEGRO", self)     
            self.__positions__[7][1] = Caballo("NEGRO", self)   
            self.__positions__[0][2] = Alfil("BLANCO", self)
            self.__positions__[0][5] = Alfil("BLANCO", self)
            self.__positions__[7][5] = Alfil("NEGRO", self) 
            self.__positions__[7][2] = Alfil("NEGRO", self)
            self.__positions__[0][4] = Rey("BLANCO", self)
            self.__positions__[7][4] = Rey("NEGRO", self)
            self.__positions__[0][3] = Reina("BLANCO", self)
            self.__positions__[7][3] = Reina("NEGRO", self)

            for col in range(8):
                self.__positions__[1][col] = Peon("BLANCO", self)
                self.__positions__[6][col] = Peon("NEGRO", self)           
    
    def __str__(self):
        board_str = ''
        for row in self.__positions__:
            row_str = ''
            for piece in row:
                if piece is None:
                    row_str += '  '  # Espacio para una casilla vacía
                else:
                    row_str += str(piece) + ' '  # Usamos el método __str__ de la pieza
            board_str += row_str + '\n'
        return board_str 
    
    def get_piece(self, row, col):
        if not (
            0 <= row < 8 or 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]

    
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    # def is_valid_coordinate(self, row, col):
    #     Verificar que las coordenadas estén en el rango válido (0 a 7)
    #     return 0 <= row < 8 and 0 <= col < 8

