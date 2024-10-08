import unittest
from juego.chess import Chess
from juego.board import Board
from juego.torre import Torre
from juego.peon import Peon
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

    def test_move_invalidturn(self):
        self.chess.__turn__ = "NEGRO" 
        with self.assertRaises(InvalidTurn):
            self.chess.move(1, 0, 2, 0)  

    def test_invalid_move(self):
        board = Board(for_test=True)
        self.chess.__board__.set_piece(0, 0, Torre("BLANCO",board))
        with self.assertRaises(InvalidMove):
            self.chess.move(0,0,1,1)  
                         
    def test_move_invalid_same_place(self):
        board = Board(for_test=True)
        self.chess.__turn__ = "BLANCO"
        self.chess.__board__.set_piece(0, 0, Torre("BLANCO",board))  
        
        with self.assertRaises(InvalidSamePlace):
            self.chess.move(0, 0, 0, 0) 

    def test_move_ivalid_move_same_color(self):
        board = Board(for_test=True)
        peon = Peon("BLANCO", board)
        torre = Torre("BLANCO", board)
        self.chess.__board__.set_piece(0, 0, peon)
        self.chess.__board__.set_piece(1, 1, torre)
        with self.assertRaises(InvalidMoveSameColor):
            self.chess.move(0,0,1,1)
               

    def test_change_turn(self):
        chess = Chess()
        self.assertEqual(chess.turn, "BLANCO")
        
        chess.change_turn()
        self.assertEqual(chess.turn, "NEGRO")

        chess.change_turn()
        self.assertEqual(chess.turn, "BLANCO")

    def test_count_pieces_initial(self):
        # Test para verificar el conteo de piezas al inicio del juego
        white_count, black_count = self.chess.count_pieces()
        self.assertEqual(white_count, 16)  # 8 peones + 8 piezas principales
        self.assertEqual(black_count, 16)  # 8 peones + 8 piezas principales

    def test_count_pieces_after_removal(self):
        # Remover una pieza blanca y verificar el conteo
        self.chess.__board__.set_piece(0, 0, None)  # Eliminar una pieza negra
        white_count, black_count = self.chess.count_pieces()
        self.assertEqual(white_count, 15)
        self.assertEqual(black_count, 16)  # Ahora hay 15 piezas negras

    def test_check_game_over_no_pieces(self):
        # Remover todas las piezas negras y verificar que el juego termina
        for row in range(8):
            for col in range(8):
                piece = self.chess.__board__.get_piece(row, col)
                if piece and piece.get_color() == "NEGRO":
                    self.chess.__board__.set_piece(row, col, None)

        self.chess.check_game_over()
        self.assertTrue(self.chess.__game_over__)
        self.assertEqual(self.chess.__winner__, "BLANCO")

    def test_check_game_over_white_wins(self):
        # Remover todas las piezas blancas y verificar que el juego termina
        for row in range(8):
            for col in range(8):
                piece = self.chess.__board__.get_piece(row, col)
                if piece and piece.get_color() == "BLANCO":
                    self.chess.__board__.set_piece(row, col, None)

        self.chess.check_game_over()
        self.assertTrue(self.chess.__game_over__)
        self.assertEqual(self.chess.__winner__, "NEGRO")    




if __name__ == '__main__':
    unittest.main()


