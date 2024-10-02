import unittest
from juego.caballo import Caballo
from juego.board import Board

class TestAlfil(unittest.TestCase):

    def test_str(self):
        board = Board()
        caballo = Caballo("BLANCO", board)
        self.assertEqual(
            str(caballo),
            "♘",
        )
    def test_valid_move_valid_white(self):
        board = Board()
        caballo = Caballo("BLANCO", board)
        self.assertTrue(caballo.valid_move(0, 1, 2, 2))  
        self.assertTrue(caballo.valid_move(0, 1, 2, 0))  
        self.assertTrue(caballo.valid_move(0, 6, 2, 7))  
        self.assertTrue(caballo.valid_move(0, 6, 2, 5)) 

    def test_valid_move_valid_black(self):
        board = Board()
        caballo = Caballo("NEGRO", board)
        self.assertTrue(caballo.valid_move(7, 1, 5, 2))  
        self.assertTrue(caballo.valid_move(7, 1, 5, 0))  
        self.assertTrue(caballo.valid_move(7, 6, 5, 5))  
        self.assertTrue(caballo.valid_move(7, 6, 5, 7))          



if __name__ == "__main__":
    unittest.main()    