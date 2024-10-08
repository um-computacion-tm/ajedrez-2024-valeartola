import unittest
from juego.piece import Piece
from juego.board import Board

class TestPiece(unittest.TestCase):
    
    def test_initialization(self):
        board = Board()
        piece = Piece("BLANCO", board)
        self.assertEqual(piece.get_color(), "BLANCO", board)
        piece = Piece("NEGRO", board)
        self.assertEqual(piece.get_color(), "NEGRO", board)

    def test_not_straight_path_ve(self):
        board = Board()
        piece = Piece("BLANCO", board)
        torre = piece._is_path_clear_straight(7,0,3,0)
        self.assertFalse(torre)

    def test_not_straight_path_ho(self):
        board = Board()
        piece = Piece("BLANCO", board)
        torre = piece._is_path_clear_straight(7,0,7,3)
        self.assertFalse(torre)

    def test_not_diagonal_path(self):
        board = Board()
        piece = Piece("BLANCO", board)
        alfil = piece._is_path_clear_diagonal(7,2,7,0)
        self.assertFalse(alfil)



if __name__ == '__main__':
    unittest.main()
