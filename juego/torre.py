from juego.piece import Piece

class Torre(Piece):
    def __str__(self):
        if self.__color__ == "BLANCO":
            return "♖"
        else:
            return "♜"

"""   def __init__(self, color):
        super().__init__(color)"""

