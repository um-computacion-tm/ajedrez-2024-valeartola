import unittest
from juego.torre import Torre
from juego.board import Board

class TestTorre(unittest.TestCase):

    def test_str(self):
        board = Board()
        torre = Torre("BLANCO", board)
        self.assertEqual(
            str(torre),
            "♖",
        )

    def test_valid_move_vertical(self):
        board = Board(for_test=True)
        torre = Torre("BLANCO", board)        
        # Movimiento válido vertical
        self.assertTrue(torre.valid_move(0, 0, 4, 0))

    def test_valid_move_horizontal(self):
        board = Board(for_test=True)
        torre = Torre("BLANCO", board)          
        # Movimiento válido horizontal
        self.assertTrue(torre.valid_move(0, 0, 0, 2))

    def test_invalid_move_diagonal(self):
        board = Board(for_test=True)
        torre = Torre("BLANCO", board)          
        # Movimiento inválido (diagonal)
        self.assertFalse(torre.valid_move(4, 4, 6, 6))

    # def test_valid_move_blocked(self):
    #     board = Board(for_test=True)
    #     torre = Torre("NEGRO", board) 
    #     board.set_piece(4,4, torre)
    #     torre_blanco = Torre("BLANCO", board) 

    #     # Suponiendo que la función _is_path_clear_straight verifica el camino
    #     # y hay una pieza bloqueando en la misma columna
    #     board.set_piece(5, 4, torre_blanco)  # Añadir una pieza para bloquear
    #     self.assertFalse(torre.valid_move(4, 4, 6, 4))



if __name__ == '__main__':
    unittest.main()