import unittest
from juego.board import Board
from juego.torre import Torre
from juego.caballo import Caballo
from juego.alfil import Alfil
from juego.peon import Peon
from juego.reina import Reina
from juego.rey import Rey
from juego.exceptions import *


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
                "    0   1   2   3   4   5   6   7\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "0 | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ | 0\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "1 | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | 1\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "2 |   |   |   |   |   |   |   |   | 2\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "3 |   |   |   |   |   |   |   |   | 3\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "4 |   |   |   |   |   |   |   |   | 4\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "5 |   |   |   |   |   |   |   |   | 5\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "6 | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | 6\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "7 | ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ | 7\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "    0   1   2   3   4   5   6   7\n"
            )
        )




    def test_move(self):
        board = Board(for_test=True)
        torre = Torre(color='BLANCO', board=board)
        board.set_piece(0, 0, torre)

        board.move(
            from_row=0,
            from_col=0,
            to_row=0,
            to_col=1,
        )

        self.assertIsInstance(
            board.get_piece(0, 1),
            Torre,
        )
        self.assertEqual(
            str(board),
            (
                "    0   1   2   3   4   5   6   7\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "0 |   | ♖ |   |   |   |   |   |   | 0\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "1 |   |   |   |   |   |   |   |   | 1\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "2 |   |   |   |   |   |   |   |   | 2\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "3 |   |   |   |   |   |   |   |   | 3\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "4 |   |   |   |   |   |   |   |   | 4\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "5 |   |   |   |   |   |   |   |   | 5\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "6 |   |   |   |   |   |   |   |   | 6\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "7 |   |   |   |   |   |   |   |   | 7\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "    0   1   2   3   4   5   6   7\n"
            )
        )


    def test_get_piece_out_of_range(self):
        board = Board(for_test=True)

        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)

        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )


if __name__ == "__main__":
    unittest.main()    