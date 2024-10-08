import unittest
from juego.peon import Peon
from juego.board import Board
from juego.alfil import Alfil


class TestPawn(unittest.TestCase):

    def test_str(self):
        board = Board()
        peon = Peon("BLANCO", board)
        self.assertEqual(
            str(peon),
            "♙",
        )

    def test_valid_move_valid_white(self):
        board = Board(for_test=True)
        peon = Peon("BLANCO", board)
        self.assertTrue(peon.valid_move(1, 0, 2, 0))  
        self.assertTrue(peon.valid_move(1, 0, 3, 0))

    def test_valid_move_valid_white_test_false(self):
        board = Board(for_test=False)
        peon = Peon("BLANCO", board)
        self.assertTrue(peon.valid_move(1, 0, 2, 0))  
        self.assertFalse(peon.valid_move(1, 0, 2, 1)) 

    def test_invalid_move_valid_white(self):
        board = Board(for_test=True)
        peon = Peon("BLANCO", board)
        self.assertFalse(peon.valid_move(1, 0, 2, 2))  
        self.assertFalse(peon.valid_move(1, 0, 2, 1))  

    def test_valid_move_eat_other_piece(self):
        board = Board(for_test=True)
        peon = Peon("BLANCO", board)
        board.set_piece(2, 0, peon)
        alfil = Alfil("NEGRO", board)
        board.set_piece(3, 1, alfil)
        self.assertTrue(peon.valid_move(2, 0, 3, 1))  


    
    




    if __name__ == "__main__":
        unittest.main()            