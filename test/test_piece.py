import unittest
from juego.piece import Piece
from juego.board import Board

class TestPiece(unittest.TestCase):
    
    def test_initialization(self):
        board = Board()
        piece = Piece("White", board)
        self.assertEqual(piece.get_color(), "White", board)
        piece = Piece("Black", board)
        self.assertEqual(piece.get_color(), "Black", board)

"""    def test_color_private_attribute(self):
        # Prueba de acceso al atributo privado
        piece = Piece("White")
        with self.assertRaises(AttributeError):
            color = piece.__color__  # Atributo privado no accesible directamente
"""
if __name__ == '__main__':
    unittest.main()
