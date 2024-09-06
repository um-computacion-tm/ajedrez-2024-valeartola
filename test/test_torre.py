import unittest
from juego.torre import Torre
from juego.board import Board
from juego.peon import Peon

class TestTorre(unittest.TestCase):

    def test_str(self):
        board = Board()
        torre = Torre("BLANCO", board)
        self.assertEqual(
            str(torre),
            "♖",
        )

    def test_move_vertical_desc(self):
        board = Board()
        torre = Torre("BLANCO", board)
        possibles = torre.possible_positions_vd(4,0)
        self.assertEqual(
                possibles,
                [(5,0), (6,0)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        torre = Torre("BLANCO",  board)
        possibles = torre.possible_positions_va(4,0)
        self.assertEqual(
                possibles,
                [(3,0), (2,0), (1,0), (0,0)]
        )        

    def test_move_horinzontal_de(self):
        board = Board()
        torre = Torre("BLANCO", board)
        possibles = torre.possible_positions_hd(4,0)
        self.assertEqual(
                possibles,
                [(4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7)]
        )

    def test_move_horinzontal_iz(self):
        board = Board()
        torre = Torre("BLANCO", board)
        possibles = torre.possible_positions_hi(4,4)
        self.assertEqual(
                possibles,
                [(4,3), (4,2), (4,1), (4,0)]
        )        






if __name__ == '__main__':
    unittest.main()