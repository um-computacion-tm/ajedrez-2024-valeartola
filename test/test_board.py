import unittest
from juego.board import Board
from juego.torre import Torre

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.board.__positions__[0][0] = Torre("BLANCO")
        self.board.__positions__[0][7] = Torre("BLANCO")
        self.board.__positions__[7][0] = Torre("NEGRO")
        self.board.__positions__[7][7] = Torre("NEGRO")        

    def test_torre_blanca1(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Torre)
        self.assertEqual(self.board.get_piece(0, 0).color, "BLANCO")
        




if __name__ == "__main__":
    unittest.main()    