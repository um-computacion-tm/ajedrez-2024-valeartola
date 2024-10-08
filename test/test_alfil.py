import unittest
from juego.alfil import Alfil
from juego.board import Board

class TestAlfil(unittest.TestCase):

    def test_str(self):
        board = Board()
        alfil = Alfil("BLANCO", board)
        self.assertEqual(
            str(alfil),
            "♗",
        )

    def test_valid_move_valid_white(self):
        board = Board(for_test=True)
        alfil = Alfil("BLANCO", board)
        self.assertTrue(alfil.valid_move(0, 2, 2, 4))  
        self.assertTrue(alfil.valid_move(0, 1, 1, 0))  
        self.assertTrue(alfil.valid_move(2, 1, 4, 3))  
        self.assertTrue(alfil.valid_move(0, 5, 2, 7)) 

    def test_invalid_move_valid_white(self):
        board = Board(for_test=True)
        alfil = Alfil("BLANCO", board)
        self.assertFalse(alfil.valid_move(0, 2, 0, 0))  
        self.assertFalse(alfil.valid_move(0, 2, 2, 2))  
        self.assertFalse(alfil.valid_move(2, 1, 4, 5))  
        self.assertFalse(alfil.valid_move(0, 5, 2, 4))         
    

if __name__ == "__main__":
    unittest.main()


