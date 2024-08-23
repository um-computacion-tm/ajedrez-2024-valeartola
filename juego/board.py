from juego.torre import Torre
from juego.caballo import Caballo
from juego.alfil import Alfil
from juego.reina import Reina
from juego.rey import Rey
from juego.peon import Peon


class Board():
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        
        piezas_blancas = [Torre, Caballo, Alfil, Reina, Rey, Alfil, Caballo, Torre]
        piezas_negras = [Torre, Caballo, Alfil, Reina, Rey, Alfil, Caballo, Torre]
        
        for i, pieza in enumerate(piezas_blancas):
            self.__positions__[0][i] = pieza("BLANCO")
            self.__positions__[1][i] = Peon("BLANCO")
        
        for i, pieza in enumerate(piezas_negras):
            self.__positions__[7][i] = pieza("NEGRO")
            self.__positions__[6][i] = Peon("NEGRO")
    
    def __str__(self):
        filas = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
                board_str += "\n"
            return board_str
    
    def get_piece(self, row, col):
        # Retorna la pieza en la coordenada especificada
        if self.is_valid_coordinate(row, col):
            return self.__positions__[row][col]
        return None
    
    def is_valid_coordinate(self, row, col):
        # Verificar que las coordenadas estén en el rango válido (0 a 7)
        return 0 <= row < 8 and 0 <= col < 8

