
from juego.chess import Chess
from juego.exceptions import InvalidMove

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)


def play(chess):
    try:
       print(chess.show_board())
       print("turno: ", chess.turn)
       from_row = int(input("From row:  "))
       from_col = int(input("From col:  "))
       to_row = int(input("To row:  "))
       to_col = int(input("To col:  "))
       chess.move(
            from_row,
            from_col,
            to_row,
            to_col
        )
    except InvalidMove as e:
        print("Movimiento invalido")

    except Exception as e:
        print("Error", e)

if __name__ == '__main__':
    main()
