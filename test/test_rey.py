import unittest
from juego.rey import Rey
from juego.board import Board

class TestRey(unittest.TestCase):

    def test_str(self):
        board = Board()
        rey = Rey("BLANCO", board)
        self.assertEqual(
            str(rey),
            "♔",
        )

    def test_valid_move_valid(self):
        board = Board()
        rey = Rey("BLANCO", board)
        # Movimiento válido en cualquier dirección
        self.assertTrue(rey.valid_move(4, 4, 5, 4))  
        self.assertTrue(rey.valid_move(4, 4, 3, 4))  
        self.assertTrue(rey.valid_move(4, 4, 4, 5))  
        self.assertTrue(rey.valid_move(4, 4, 4, 3))  
        self.assertTrue(rey.valid_move(4, 4, 5, 5))  
        self.assertTrue(rey.valid_move(4, 4, 3, 3))  

    def test_valid_move_invalid(self):
        board = Board()
        rey = Rey("BLANCO", board)
        # Movimiento inválido (más de una casilla)
        self.assertFalse(rey.valid_move(4, 4, 6, 4))  
        self.assertFalse(rey.valid_move(4, 4, 4, 6))  
        self.assertFalse(rey.valid_move(4, 4, 6, 6))  

    def test_valid_move_no_movement(self):
        board = Board()
        rey = Rey("BLANCO", board)
        # No se mueve
        self.assertFalse(rey.valid_move(4, 4, 4, 4))

if __name__ == "__main__":
    unittest.main()
