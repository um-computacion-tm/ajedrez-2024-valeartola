from juego.piece import Piece

class Reina(Piece):
    def __str__(self):
        if self.__color__ == "BLANCO":
            return "♕"
        else:
            return "♛"