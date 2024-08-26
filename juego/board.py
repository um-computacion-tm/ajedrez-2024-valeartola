from juego.torre import Torre
from juego.caballo import Caballo
from juego.alfil import Alfil
from juego.reina import Reina
from juego.rey import Rey
from juego.peon import Peon


class Board():
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Torre("BLANCO") 
        self.__positions__[0][7] = Torre("BLANCO")         
        self.__positions__[7][7] = Torre("NEGRO")      
        self.__positions__[7][0] = Torre("NEGRO")  
        self.__positions__[0][1] = Caballo("BLANCO")
        self.__positions__[0][6] = Caballo("BLANCO")        
        self.__positions__[7][6] = Caballo("NEGRO")     
        self.__positions__[7][1] = Caballo("NEGRO")   
        self.__positions__[0][2] = Alfil("BLANCO")
        self.__positions__[0][5] = Alfil("BLANCO")
        self.__positions__[7][5] = Alfil("NEGRO") 
        self.__positions__[7][2] = Alfil("NEGRO")
        self.__positions__[0][3] = Rey("BLANCO")
        self.__positions__[7][3] = Rey("NEGRO")
        self.__positions__[0][4] = Reina("BLANCO")
        self.__positions__[7][4] = Reina("NEGRO")

        for col in range(8):
            self.__positions__[1][col] = Peon("BLANCO")
            self.__positions__[6][col] = Peon("NEGRO")           
    
    def __str__(self):
        board_str = ""
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

