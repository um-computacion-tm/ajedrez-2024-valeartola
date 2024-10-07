from juego.chess import Chess
from juego.exceptions import InvalidMove
from juego.exceptions import Withoutcoordinate

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)
    print("El ganador es " + chess.winner)


def play(chess):
    try:
       print("---------------AJEDREZ---------------")
       print(chess.show_board())
       print("turno: ", chess.turn)
       offer_draw = input("¿Deseas ofrecer un empate? (si/no): ").strip().lower()
       if offer_draw == 'si':
            chess.offer_draw()  
            return False
       from_row = int(input("Desde la fila:  "))
       from_col = int(input("Desde la columna:  "))
       to_row = int(input("A la fila:  "))
       to_col = int(input("A la columna:  "))
    #    if from_row.strip() == '' or from_col.strip() == '' or to_row.strip() == '' or to_col.strip() == '':
    #         raise Withoutcoordinate
       chess.move(
            from_row,
            from_col,
            to_row,
            to_col
        )
    except InvalidMove as e:
        print (e)

    except Exception as e:
        print("Error", e)



if __name__ == '__main__':
    main()
