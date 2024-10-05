import unittest
from juego.chess import Chess
from juego.board import Board
from juego.torre import Torre
from juego.exceptions import InvalidCoordinate, EmptyPosition, InvalidTurn, InvalidMove, InvalidSamePlace, InvalidMoveSameColor

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()
        self.board = Board()        

    def test_is_playing(self):
        chess = Chess()
        self.assertTrue(chess.is_playing())

    def test_first_turn(self):
        self.assertEqual(self.chess.__turn__, "BLANCO")

    def test_move_invalidcoordinate(self):
        with self.assertRaises(InvalidCoordinate):
            self.chess.move(-1, 0, 0, 0) 

    def test_no_piece_at_start_raises_error(self):
        from_row, from_col, to_row, to_col = 3, 3, 5, 2  
        with self.assertRaises(EmptyPosition):
            self.chess.move(from_row, from_col, to_row, to_col)    

    def test_invalid_move(self):
        Board(for_test=True)
        self.chess.__board__.set_piece(0, 0, Torre("WHITE",Board(for_test=True)))
        with self.assertRaises(InvalidMove):
            self.chess.move(0,0,1,1)

    def test_move_invalidturn(self):
        self.chess.__turn__ = "NEGRO" 
        with self.assertRaises(InvalidTurn):
            self.chess.move(1, 0, 2, 0)  

    def test_invalid_move_same_color(self):
        Board(for_test=True)
        self.chess.__board__.set_piece(0, 0, Torre("BLANCO",Board(for_test=True)))
        with self.assertRaises(InvalidMoveSameColor):
            self.chess.move(0,0,1,1)  
                         
       
    def test_move_invalid_same_place(self):
        Board(for_test=True)
        self.chess.__turn__ = "BLANCO"
        self.chess.__board__.set_piece(0, 0, Torre("BLANCO",Board(for_test=True)))  
        
        with self.assertRaises(InvalidSamePlace):
            self.chess.move(0, 0, 0, 0)        


    def test_change_turn(self):
        chess = Chess()
        self.assertEqual(chess.turn, "BLANCO")
        
        chess.change_turn()
        self.assertEqual(chess.turn, "NEGRO")
        
        chess.change_turn()
        self.assertEqual(chess.turn, "BLANCO")




if __name__ == '__main__':
    unittest.main()


