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
    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Peon("WHITE", board))
        torre = Torre("WHITE", board)
        board.set_piece(4, 1, Torre)
        possibles = torre.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Peon("BLACK", board))
        torre = Torre("WHITE", board)
        board.set_piece(4, 1, Torre)
        possibles = torre.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

    def test_move_diagonal_desc(self):
        board = Board()
        torre = board.get_piece(col=0, row=0)
        is_possible = torre.valid_positions(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )

        self.assertFalse(is_possible)





if __name__ == '__main__':
    unittest.main()