import unittest
from juego.alfil import Alfil
from juego.board import Board

class TestTorre(unittest.TestCase):

    def test_str(self):
        board = Board()
        alfil = Alfil("BLANCO", board)
        self.assertEqual(
            str(alfil),
            "♗",
        )

    def test_move_vertical_desc(self):
        board = Board()
        alfil = Alfil("BLANCO", board)
        possibles = alfil.possible_positions(4,0)
        self.assertEqual(
                possibles,
                [(5,1), (6,2), (3,1), (2,2)]
        )   
     



if __name__ == "__main__":
    unittest.main()    