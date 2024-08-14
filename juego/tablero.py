from juego.fichas.torre import Torre

class Tablero():
    def __init__(self):
        self.__positions__ = []
        for _ in range(7):
            col = []
            for _ in range(7):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Torre("BLANCO") #White
        self.__positions__[0][7] = Torre("BLANCO") #White        
        self.__positions__[7][7] = Torre("NEGRO") #Black     
        self.__positions__[7][0] = Torre("NEGRO") #Black       

    def get_piece(self, row, col):
        return self.tablero.__positions__[row][col]        