import unittest
from juego.rey import Rey
from juego.board import Board

class TestRey(unittest.TestCase):

    def test_str(self):
        board = Board()
        rey = Rey("BLANCO", board)
        self.assertEqual(
            str(rey),
            "♔",
        )


if __name__ == "__main__":
    unittest.main()
