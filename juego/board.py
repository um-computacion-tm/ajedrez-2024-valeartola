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
        # Encabezado y pie con los números de las columnas espaciados
        header_footer = "    " + "   ".join(str(i) for i in range(8)) + "\n"
        board_str = header_footer
        board_str += "  +" + "---+" * 8 + "\n"  # Línea superior del tablero
        
        # Construir el tablero con las piezas y las casillas vacías
        for i, row in enumerate(self.__positions__):
            board_str += f"{i} |"  # Añadir el número de fila al inicio
            for cell in row:
                if cell is None:
                    board_str += "   |"  # Representación de casilla vacía
                else:
                    board_str += f" {str(cell)} |"  # Representación de la pieza
            board_str += f" {i}\n"  # Añadir el número de fila al final
            board_str += "  +" + "---+" * 8 + "\n"  # Añadir la línea divisoria entre filas
        
        board_str += header_footer  
        return board_str

    def is_valid_coordinate(self, row, col):
        return 0 <= row <= 8 and 0 <= col <= 8

    def get_piece(self, row, col):
        if not self.is_valid_coordinate(row, col):
            raise OutOfBoard()
        return self.__positions__[row][col]
    
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)
        if isinstance(origin, Peon) and (to_row == 0 or to_row == 7):
            self.set_piece(to_row, to_col, Reina(origin.__color__, self))


