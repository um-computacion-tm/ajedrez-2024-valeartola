from juego.chess import Chess
from juego.exceptions import InvalidMove
from juego.exceptions import Withoutcoordinate
from juego.exceptions import NoneEmpate

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
       offer_draw = ""
       while (offer_draw not in ("si", "no")):
            offer_draw = input("¿Deseas ofrecer un empate? (si/no): ").strip().lower()
            if offer_draw == 'si':
                    chess.change_turn()
                    print(f"turno: {chess.__turn__}")
                    accept_draw = ""
                    while (accept_draw not in ("si", "no")):
                        accept_draw = input("¿Acepta empate? (si/no): ").strip().lower()
                    if accept_draw == "si":
                        print("Ambos jugadores han acordado un empate.")
                        print("---------------------")  
                        chess.__game_over__ = True
                        chess.__winner__ = "Ninguno"
                        return

       
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
