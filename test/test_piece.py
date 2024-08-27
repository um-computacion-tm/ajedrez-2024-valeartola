import unittest
from juego.piece import Piece

class TestPiece(unittest.TestCase):
    
    def test_initialization(self):
        piece = Piece("White")
        self.assertEqual(piece.get_color(), "White")
        piece = Piece("Black")
        self.assertEqual(piece.get_color(), "Black")

"""    def test_color_private_attribute(self):
        # Prueba de acceso al atributo privado
        piece = Piece("White")
        with self.assertRaises(AttributeError):
            color = piece.__color__  # Atributo privado no accesible directamente
"""
if __name__ == '__main__':
    unittest.main()
