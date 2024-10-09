import sys
sys.path.append("src")
from Logic.NavalWarfare import NavalWarfare, Player

def imprimir_tablero(matrix):
    letras = "ABCDE"
    print("  " + " ".join(letras[:len(matrix[0])]))
    for idx, row in enumerate(matrix):
        print(f"{idx + 1} " + " ".join(str(cell) for cell in row))
                    
def imprimir_tablero_oculto(matrix):
    letras = "ABCDE"
    print("  " + " ".join(letras[:len(matrix[0])]))
    for idx, row in enumerate(matrix):
        fila = ["2" if cell == 2 else "-1" if cell == -1 else "0" for cell in row]
        print(f"{idx + 1} " + " ".join(fila))
        

def main():
    player1 = Player(input("Ingrese el nombre del jugar 1: "))
    player2 = Player(input("Ingrese el nombre del jugador 2: "))

    juego = NavalWarfare(player1, player2)
    for i in range(2):
        print(f"///////////////////////////////////////////")
        print(f"Tablero del jugador {juego.currentplayer.name}")
        if juego.currentplayer.ships == 3:
            imprimir_tablero(juego.currentplayer.board)
            for i in range(juego.currentplayer.ships):
                if juego.currentplayer.ships != 0:
                    juego.posicionate_ship(input("Ingrese una locación por ejemplo A1: "))
                    imprimir_tablero(juego.currentplayer.board)
            juego.update_current_player()
    juego.attack_board()
    while juego.Player1.ships_in_game > 0 and juego.Player2.ships_in_game > 0:
        print(f"Comienza atacando el jugador {juego.currentplayer.name}")
        imprimir_tablero_oculto(juego.currentplayer.board_attack)
        if juego.shoot(input(f"Jugador: {juego.currentplayer.name} Ingrese una locacion para atacar (ej: A1): ")):
            print(f"Le has dado")
        else:
            print(f"No le has dado")
        imprimir_tablero_oculto(juego.currentplayer.board_attack)
        if juego.game_over() == True:
            if juego.Player1.ships_in_game > 0 and juego.Player2.ships_in_game == 0:
                print(f"Gano el jugador {juego.Player1.name}")
            elif juego.Player2.ships_in_game > 0 and juego.Player1.ships_in_game == 0:
                print(f"Gano el jugador {juego.Player2.name}")
        juego.update_current_player()
main()