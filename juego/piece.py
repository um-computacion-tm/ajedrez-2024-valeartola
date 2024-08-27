class Piece():
    def __init__(self,color, board):
        self.__color__ = color
        self.__board__ = board

    def get_color(self):
        return self.__color__
    
    def __str__(self):
        if self.__color__ == "BLANCO":
            return self.white_str
        else:
            return self.black_str