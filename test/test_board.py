import unittest
from juego.board import Board
from juego.torre import Torre
from juego.caballo import Caballo
from juego.alfil import Alfil
from juego.peon import Peon
from juego.reina import Reina
from juego.rey import Rey

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        tablero = Board()
        
        # Verificar posiciones de piezas blancas
        piezas_blancas = [Torre, Caballo, Alfil, Reina, Rey, Alfil, Caballo, Torre]
        for i, pieza in enumerate(piezas_blancas):
            self.assertIsInstance(tablero.__positions__[0][i], pieza)
            self.assertEqual(tablero.__positions__[0][i].__color__, "BLANCO")
            self.assertIsInstance(tablero.__positions__[1][i], Peon)
            self.assertEqual(tablero.__positions__[1][i].__color__, "BLANCO")
        
        # Verificar posiciones de piezas negras
        piezas_negras = [Torre, Caballo, Alfil, Reina, Rey, Alfil, Caballo, Torre]
        for i, pieza in enumerate(piezas_negras):
            self.assertIsInstance(tablero.__positions__[7][i], pieza)
            self.assertEqual(tablero.__positions__[7][i].__color__, "NEGRO")
            self.assertIsInstance(tablero.__positions__[6][i], Peon)
            self.assertEqual(tablero.__positions__[6][i].__color__, "NEGRO")
        
        # Verificar que el resto del tablero esté vacío
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(tablero.__positions__[row][col])
 


    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
                "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
                "                \n"
                "                \n"
                "                \n"
                "                \n"
                "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
                "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
            )
        )




if __name__ == "__main__":
    unittest.main()    