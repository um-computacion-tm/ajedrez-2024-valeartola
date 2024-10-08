import unittest
from juego.reina import Reina
from juego.board import Board

class TestReina(unittest.TestCase):

    def test_str(self):
        board = Board()
        reina = Reina("BLANCO", board)
        self.assertEqual(
            str(reina),
            "♕",
        )

    def test_valid_move_valid_white(self):
        board = Board(for_test=True)
        reina = Reina("BLANCO", board)
        self.assertTrue(reina.valid_move(0, 3, 2, 3))  
        self.assertTrue(reina.valid_move(0, 3, 0, 1))  
        self.assertTrue(reina.valid_move(0, 3, 1, 4))  
        self.assertTrue(reina.valid_move(0, 3, 1, 2)) 

    def test_valid_move_valid_black(self):
        board = Board(for_test=True)
        reina = Reina("NEGRO", board)
        self.assertTrue(reina.valid_move(7, 3, 5, 3))  
        self.assertTrue(reina.valid_move(7, 3, 6, 2))  
        self.assertTrue(reina.valid_move(7, 3, 6, 4))  
        self.assertTrue(reina.valid_move(7, 3, 7, 5)) 

    def test_valid_move_invalid_white(self):
        board = Board(for_test=True)
        reina = Reina("BLANCO", board)
        self.assertFalse(reina.valid_move(0, 3, 2, 0))  
        self.assertFalse(reina.valid_move(0, 3, 1, 5))  
        self.assertFalse(reina.valid_move(0, 3, 2, 6))  
        self.assertFalse(reina.valid_move(0, 3, 1, 1)) 

    def test_valid_move_invalid_black(self):
        board = Board(for_test=True)
        reina = Reina("NEGRO", board)
        self.assertFalse(reina.valid_move(7, 3, 6, 1))  
        self.assertFalse(reina.valid_move(7, 3, 6, 5))  
        self.assertFalse(reina.valid_move(7, 3, 4, 7))  
        self.assertFalse(reina.valid_move(7, 3, 3, 1)) 



if __name__ == "__main__":
    unittest.main()
