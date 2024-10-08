class InvalidMove(Exception):
    message = "Movimieto de pieza invalido"
    def __str__(self):
        return self.message
    
class InvalidCoordinate(Exception):
    message = "Coordenada invalida"

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posición esta vacia"

class OutOfBoard(InvalidMove):
    message = "La posición indicada se encuentra fuera del tablero"

class InvalidMoveSameColor(InvalidMove):
    message = "No puedes capturar una pieza de tu mismo color"

class InvalidSamePlace(InvalidMove):
    message = "No puede mover una pieza en su misma posición "

class OutOfBoard(InvalidMove):
    message = "La posición indicada se encuentra fuera del tablero"

class Withoutcoordinate(InvalidMove):
    message = "Coordenada vacia"

