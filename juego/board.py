from juego.fichas.torre import Torre
from juego.fichas.caballo import Caballo
from juego.fichas.alfin import Alfin

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
        self.__positions__[0][2] = Alfin("BLANCO")
        self.__positions__[0][5] = Alfin("BLANCO")
        self.__positions__[7][5] = Alfin("NEGRO") 
        self.__positions__[7][2] = Alfin("NEGRO")              

    def get_piece(self, row, col):
        return self.board.__positions__[row][col]        