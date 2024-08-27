import unittest
from juego.chess import Chess


class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_turno_inicial(self):
        self.assertEqual(self.chess.__turn__, "BLANCO")








if __name__ == '__main__':
    unittest.main()


