from juego.board import Board

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "BLANCO"
    
    def move(self,
            from_row,
            from_col,
            to_row,
            to_col,
        ):
            #validar coordenadas
            piece = self.board.get_piece(from_row, from_col)
            self.change_turn()
    @property  
    def turn(self):
         return self.__turn__

    def change_turn(self):
        if self.__turn__ == "BLANCO":
            self.__turn__ == "NEGRO"
        else:
            self.__turn__ == "BLANCO"             
